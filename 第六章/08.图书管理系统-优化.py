"""
图书馆管理系统（优化版）
功能：会员登录、借书、还书、查看借阅记录，数据持久化到 JSON。
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional
import json


# ========================= 全局配置 =========================
DATA_DIR = Path(__file__).resolve().parent / "data"
BOOKS_FILE = DATA_DIR / "books.json"
MEMBERS_FILE = DATA_DIR / "members.json"

NORMAL_LIMIT = 3            # 普通会员可借数量
VIP_BASE_LIMIT = 6          # VIP 基础可借数量（实际 = 基础 + vip_level）
MAX_LOGIN_ATTEMPTS = 3      # 最大登录尝试次数


# ========================= 图书 =========================
class Book:
    """图书实体类"""

    def __init__(self, book_id: str, title: str, author: str,
                 total_num: int, available_num: Optional[int] = None):
        self.book_id = book_id          # 图书编号
        self.title = title              # 图书名称
        self.author = author            # 图书作者
        self.total_num = total_num      # 图书总数
        self.__available_num = total_num if available_num is None else available_num

    def borrow_book(self) -> bool:
        """尝试借出一本，成功返回 True"""
        if self.__available_num <= 0:
            return False
        self.__available_num -= 1
        return True

    def return_book(self) -> bool:
        """归还一本，成功返回 True"""
        if self.__available_num >= self.total_num:
            return False
        self.__available_num += 1
        return True

    def get_available_num(self) -> int:
        return self.__available_num

    def to_dict(self) -> dict:
        return {
            "编号": self.book_id,
            "标题": self.title,
            "作者": self.author,
            "数量": self.total_num,
            "可用数量": self.__available_num,
        }


# ========================= 会员 =========================
class Member(ABC):
    """会员抽象基类：规定子类必须实现 get_max_books()"""

    def __init__(self, member_id: str, name: str, password: str):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrowed_books: List[Book] = []

    # ---------- 核心业务 ----------
    def borrow_book(self, book: Book) -> bool:
        if self.__has_borrowed(book):
            print(f"借阅失败！《{book.title}》已在您的借阅列表中")
            return False
        if len(self.__borrowed_books) >= self.get_max_books():
            print(f"借阅失败！您最多可借 {self.get_max_books()} 本，"
                  f"当前已借 {len(self.__borrowed_books)} 本")
            return False
        if not book.borrow_book():
            print(f"借阅失败！《{book.title}》已全部借出")
            return False
        self.__borrowed_books.append(book)
        print(f"借阅成功！已借阅《{book.title}》")
        return True

    def return_book(self, book: Book) -> bool:
        target = next((b for b in self.__borrowed_books
                       if b.book_id == book.book_id), None)
        if target is None:
            print(f"归还失败！您并未借阅《{book.title}》")
            return False
        self.__borrowed_books.remove(target)
        target.return_book()
        print(f"归还成功！已归还《{target.title}》")
        return True

    def __has_borrowed(self, book: Book) -> bool:
        return any(b.book_id == book.book_id for b in self.__borrowed_books)

    # ---------- 属性访问 ----------
    def get_password(self) -> str:
        return self.__password

    def get_borrowed_books(self) -> List[Book]:
        return list(self.__borrowed_books)  # 返回副本，避免外部直接修改

    def _restore_borrowed_books(self, books: List[Book]) -> None:
        """仅供数据加载时恢复借阅记录使用"""
        self.__borrowed_books = list(books)

    # ---------- 序列化 ----------
    def to_dict(self) -> dict:
        return {
            "卡号": self.member_id,
            "姓名": self.name,
            "密码": self.__password,
            "借阅": [b.book_id for b in self.__borrowed_books],
        }

    # ---------- 抽象方法 ----------
    @abstractmethod
    def get_max_books(self) -> int:
        """返回当前会员最大可借阅数量"""
        raise NotImplementedError


class NormalMember(Member):
    """普通会员"""

    def get_max_books(self) -> int:
        return NORMAL_LIMIT


class VIPMember(Member):
    """VIP 会员"""

    def __init__(self, member_id: str, name: str, password: str, vip_level: int):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level

    def get_max_books(self) -> int:
        return VIP_BASE_LIMIT + self.vip_level

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["会员等级"] = self.vip_level
        return data


# ========================= 系统 =========================
class LibrarySystem:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        self.current_member: Optional[Member] = None
        self._load_data()

    # ---------------- 数据加载 ----------------
    def _load_data(self) -> None:
        self._load_books()
        self._load_members()

    def _load_books(self) -> None:
        if not BOOKS_FILE.exists():
            raise FileNotFoundError(f"未找到图书数据文件：{BOOKS_FILE}")
        with BOOKS_FILE.open("r", encoding="utf-8") as f:
            books_data = json.load(f)
        for item in books_data:
            book = Book(
                item["编号"], item["标题"], item["作者"], item["数量"],
                item.get("可用数量"),  # 兼容老数据：无此字段时按总数处理
            )
            self.books[book.book_id] = book
        print(f"加载图书数据成功（共 {len(self.books)} 本）")

    def _load_members(self) -> None:
        if not MEMBERS_FILE.exists():
            raise FileNotFoundError(f"未找到会员数据文件：{MEMBERS_FILE}")
        with MEMBERS_FILE.open("r", encoding="utf-8") as f:
            members_data = json.load(f)
        for item in members_data:
            member_id = item["卡号"]
            if member_id.startswith("N"):
                member: Member = NormalMember(member_id, item["姓名"], item["密码"])
            elif member_id.startswith("V"):
                member = VIPMember(member_id, item["姓名"], item["密码"], item["会员等级"])
            else:
                print(f"[警告] 未知会员类型，已跳过：{member_id}")
                continue
            # 恢复借阅记录（把 book_id 还原成 Book 对象）
            borrowed = [self.books[bid] for bid in item.get("借阅", [])
                        if bid in self.books]
            member._restore_borrowed_books(borrowed)
            self.members[member_id] = member
        print(f"加载会员数据成功（共 {len(self.members)} 人）")

    # ---------------- 数据保存 ----------------
    def _save_data(self) -> None:
        self._save_books()
        self._save_members()

    def _save_books(self) -> None:
        with BOOKS_FILE.open("w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books.values()],
                      f, ensure_ascii=False, indent=2)

    def _save_members(self) -> None:
        with MEMBERS_FILE.open("w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in self.members.values()],
                      f, ensure_ascii=False, indent=2)

    # ---------------- 登录 ----------------
    def login(self) -> bool:
        for attempt in range(MAX_LOGIN_ATTEMPTS):
            member_id = input("请输入会员卡号：").strip()
            member = self.members.get(member_id)
            if member is None:
                print(f"会员卡号不存在（剩余 {MAX_LOGIN_ATTEMPTS - attempt - 1} 次）")
                continue
            password = input("请输入密码：").strip()
            if password != member.get_password():
                print(f"密码错误（剩余 {MAX_LOGIN_ATTEMPTS - attempt - 1} 次）")
                continue
            self.current_member = member
            print(f"登录成功，欢迎 {member.name}！")
            return True
        print("登录尝试次数过多，程序退出")
        return False

    # ---------------- 业务操作 ----------------
    def borrow_book(self) -> None:
        self._show_books()
        book_id = input("请输入要借阅的图书编号：").strip()
        book = self.books.get(book_id)
        if book is None:
            print("图书编号不存在！")
            return
        if self.current_member.borrow_book(book):
            self._save_data()

    def return_book(self) -> None:
        self.show_borrowed_books()
        book_id = input("请输入要归还的图书编号：").strip()
        book = self.books.get(book_id)
        if book is None:
            print("图书编号不存在！")
            return
        if self.current_member.return_book(book):
            self._save_data()

    def show_borrowed_books(self) -> None:
        books = self.current_member.get_borrowed_books()
        if not books:
            print("【提示】当前没有借阅任何图书")
            return
        print("\n【已借阅的图书列表】")
        for book in books:
            print(f"  编号：{book.book_id}  《{book.title}》")

    # ---------------- 打印辅助 ----------------
    def _show_books(self) -> None:
        print("\n【图书馆藏书列表】")
        for book in self.books.values():
            print(f"  编号：{book.book_id}  《{book.title}》  "
                  f"作者：{book.author}  总数：{book.total_num}  "
                  f"可借：{book.get_available_num()}")

    # ---------------- 主菜单 ----------------
    def run(self) -> None:
        if not self.login():
            return

        handlers = {
            "1": self.borrow_book,
            "2": self.return_book,
            "3": self.show_borrowed_books,
        }
        while True:
            print("\n" + "=" * 30)
            print("1. 借阅图书")
            print("2. 归还图书")
            print("3. 查看已借阅图书")
            print("4. 退出系统")
            print("=" * 30)
            choice = input("请输入你的选择：").strip()
            if choice == "4":
                print("退出系统，感谢使用！")
                break
            handler = handlers.get(choice)
            if handler is None:
                print("无效的选择，请重新输入")
            else:
                handler()


if __name__ == "__main__":
    try:
        LibrarySystem().run()
    except FileNotFoundError as e:
        print(f"[错误] {e}")