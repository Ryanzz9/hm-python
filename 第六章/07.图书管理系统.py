from abc import ABC, abstractmethod
import json


class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id # 图书编号
        self.title = title # 图书名称
        self.author = author # 图书作者
        self.total_num = total_num # 图书总数
        self.__available_num = total_num # 可用图书数量

    def borrow_book(self): # 借阅图书
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    def return_book(self): # 归还图书
        self.__available_num += 1


    def get_available_num(self):
        return self.__available_num

# #抽象类：是一种只能被继承，不能被直接实例化的类，作用就是规定子类必须要实现哪些方式，强制子类必须遵守统一的代码规范
# Python中的抽象类，需要继承 abc 模块中的ABC类 ---> ABC:Abstract Base Class
# 会员类
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id # 会员编号
        self.name = name # 会员姓名
        self.__password = password # 会员密码
        self.__borrowed_books = [] # 已借阅图书列表

    def borrow_book(self, book:Book):
        # 判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败！当前会员借阅数量已达到最大限制")
            return False
        # 判断书籍是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"借阅成功！已借阅图书：{book.title}")
            return True
        else:
            print("借阅失败！书籍已被借完")
            return False

    #归还图书
    def return_book(self, book:Book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
            print(f"归还成功！已归还图书：{book.title}")
        else:
            print("归还失败！未借阅该图书")


    def get_password(self):
        return self.__password


    def get_borrowed_books(self):
        return self.__borrowed_books

    # 获取会员最大借阅数量(需要在子类中实现)
    @abstractmethod #标识抽象方法
    def get_max_books(self)->int:
        pass

class NormalMember(Member):
    def get_max_books(self)->int:
        return 3

class VIPMember(Member):
    def __init__(self, member_id, name, password,vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level # vip等级

    def get_max_books(self) ->int:
        return 6 + self.vip_level


class LibrarySystem:
    def __init__(self):
        self.books = {} # 图书列表
        self.members = {} # 会员列表
        self.current_member: Member | None = None # 当前登录的会员
        #加载数据（书籍/会员）
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        with open('data/books.json', 'r', encoding='utf-8') as f:
            books_data = json.load(f)
        for book in books_data:
            self.books[book["编号"]] = Book(book["编号"], book["标题"], book["作者"], book["数量"])
        print(f"加载图书数据成功")


    # 将 JSON 字典 转换为 会员对象，并存入 self.members
    def load_members_data(self):
        with open('data/members.json', 'r', encoding='utf-8') as f:
            members_data = json.load(f)
        for member in members_data:
            if member['卡号'].startswith('N'):
                self.members[member['卡号']] = NormalMember(member['卡号'], member['姓名'], member['密码'])
            elif member['卡号'].startswith('V'):
                self.members[member['卡号']] = VIPMember(member['卡号'], member['姓名'], member['密码'], member['会员等级'])
        print(f"加载会员数据成功")
        # self.members 字典中，key 是字符串（member['卡号']，比如 "N001"）
        # value 是 Member 类型（及其子类）的对象实例
        # 因为 NormalMember 和 VIPMember 都继承自 Member。




    def login(self):
        while True:
            member_id = input("请输入会员卡号：")
            if member_id not in self.members:
                print("会员卡号不存在，请重新输入")
                continue
            password = input("请输入密码：")
            if password != self.members[member_id].get_password():
                print("密码错误，请重新输入")
                continue
            self.current_member = self.members[member_id]
            print(f"登录成功，欢迎{self.current_member.name}")
            return True


    def borrow_book(self):#借阅图书
        # 1. 展示出当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号：{book.book_id}, 标题：{book.title}, 作者：{book.author}, 数量：{book.total_num}, 可用数量：{book.get_available_num()}")

        # 2.获取用户输入的图书编号，执行借书操作
        book_id = input("请输入要借阅的图书编号：")
        if book_id not in self.books:
            print("图书编号不存在，请重新输入")
            return
        self.current_member.borrow_book(self.books[book_id])
        print("借书操作完成")

    def return_book(self):
    # 1.展示出当前会员的借阅列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("【已借阅的图书列表:】")
        for book in borrowed_books:
            print(f"编号：{book.book_id}, 标题：{book.title}")

        # 2.获取用户输入的图书编号，执行还书操作
        book_id = input("请输入图书编号：")
        if book_id not in self.books:
            print("图书编号不存在，请重新输入")
            return
        self.current_member.return_book(self.books[book_id])
        print("还书操作完成")


    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("【已借阅的图书列表:】")
            for book  in borrowed_books:
                print(f"编号：{book.book_id}, 标题：{book.title}")
        else:
            print("【提示】当前没有借阅任何图书")

    def run(self):
        if self.login():
            while True:
                print("1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看已借阅图书")
                print("4. 退出系统")


                choice = input("请输入你的选择：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统")
                        break
                    case _:
                        print("无效的选择，请重新输入")


if __name__ == '__main__':
    library_system = LibrarySystem()
    library_system.run()