# 异常处理


# try:
#     print("= "*40)
#     print(my_name)
#     print("+"*40)
#
# except NameError as e:
#     print("程序运行出错了，请练习管理员！异常信息：",e)
#
#
#
# try:
#     print("= "*40)
#     print("ABC".hello)
#     #print("ABC"[8])
#     #print(1/0)
#     print("+"*40)
#
# # ZeroDivisionError: division by zero
# except NameError as e:
#     print("名字不存在，请检查变量或函数名，异常信息：",e)
#
# except ZeroDivisionError as e:
#     print("0不能做被除数，异常信息：",e)
#
# #IndexError: string index out of range
#
# except IndexError as e:
#     print("索引错误，异常信息：", e)
#
#
# except Exception as e:
#     print("程序运行出错了，请联系管理员，错误信息：",e)
#
#
# finally:
#     #无论程序是否正常运行，finally代码块中的代码都会运行
#     print("资源释放~")


## 异常传递

# def fun1():
#     print("fun1 ...running...")
#     fun2()
#
# def fun2():
#     print("fun2 ...running...")
#     fun3()
#
# def fun3():
#     print("fun3 ...running...")
#     print(my_name)
#
# if __name__ == "__main__":
#     try:
#         fun1()
#     except Exception as e:
#         print("运行错误，错误信息：",e)
#

##教务系统增加错误处理
## 学生类

class Student:
    def __init__(self,name,math,chinese,english):
        self.name=name
        self.math=math
        self.chinese = chinese
        self.english = english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分: {self.chinese + self.math + self.english}"

    # 修改学生的成绩

    def update_score(self,chinese=None,english=None,math=None):
        if chinese is not None:
            self.chinese = chinese

        if english is not None:
            self.english = english
        if math is not None:
            self.math = math
# 教务管理系统

class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []# 列表，记录的是在校学生的成绩信息

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生的姓名：")
        # 判断学生姓名是否存在，如果存在，则添加失败不能重复添加
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在添加失败")
                return
        chinese = int(input("请输入学生的语文成绩："))
        math = int(input("请输入学生的数学成绩："))
        english = int(input("请输入学生的英语成绩："))


        #判断分时是否在0-100之间

        if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
          stu = Student(name,chinese,math,english)
          self.student_list.append(stu)
          print("学生信息添加成功")

        else:
          print("输入错误，成绩必须在0-100之间")

    #修改学生信息
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        # 判断学生姓名是否存在，如果存在，则添加失败不能重复添加
        for s in self.student_list:
            if s.name == name:
               print(f"当前成绩：{s}")
               chinese = int(input("请输入学生的语文成绩："))
               math = int(input("请输入学生的数学成绩："))
               english = int(input("请输入学生的英语成绩："))

               if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                   s.update_score(chinese,math,english)
                   print("学生信息添加成功")
                   print(f"修改后的成绩：{s}")
                   return

               else:
                   print("输入错误，成绩必须在0-100之间")
                   return
        print("未找到该学生，修改失败！")


    #删除学生信息
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        # 判断学生姓名是否存在，如果存在，则添加失败不能重复添加
        for s in self.student_list:
            if s.name == name:
               self.student_list.remove(s)
            print("删除学生信息成功！")
            return
        print("未找到该学生，删除失败！")



    # 查询指定学生信息
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        # 判断学生姓名是否存在，如果存在，则添加失败不能重复添加
        for s in self.student_list:
            if s.name == name:
               print(f"{s}")
               return

        print("查询的学生不存在")


    #所有学生信息
    def list_student(self):
        for s in self.student_list:
               print(f"{s}")
               return




    def run(self):
        print(f"还原使用教务管理系统V{EduManagement.system_version}")
        try:
            while True:
                print()
                print("####################################################################")
                print("1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统#")
                print("####################################################################")


                choice = input("\n请输入要执行的操作1-6：")
                match choice:
                    case "1":
                       self.add_student()
                    case "2":
                       self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("bye")
                        break
                    case _:
                        print("输入非法")
        except ValueError:
            print("输入的数据有问题，请检查并重新选择")
        except Exception:
            print("程序运行出错了，请重新选择")

if __name__ == '__main__':
   edu_management = EduManagement()
   edu_management.run()