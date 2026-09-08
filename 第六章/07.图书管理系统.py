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


    def get_available_num(self): # 获取可用图书数量
        return self.__available_num
