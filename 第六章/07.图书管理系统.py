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


# 会员类
class Member:
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
