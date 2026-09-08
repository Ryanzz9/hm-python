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



    def load_members_data(self):
        with open('data/members.json', 'r', encoding='utf-8') as f:
            members_data = json.load(f)
        for member in members_data:
            if member['卡号'].startswith('N'):
                self.members[member['卡号']] = NormalMember(member['卡号'], member['姓名'], member['密码'])
            elif member['卡号'].startswith('V'):
                self.members[member['卡号']] = VIPMember(member['卡号'], member['姓名'], member['密码'], member['会员等级'])
        print(f"加载会员数据成功")


if __name__ == '__main__':
    library_system = LibrarySystem()
    print(library_system.books)
    print(library_system.members)