
##__all__ 指定 from .. import * 导入的是哪业力能
__all__ = ["log_separator1", "log_separator2", "log_separator3", "log_separator4"]



# 函数
def log_separator1():
    print("- " * 30)
def log_separator2():
    print("+ " * 30)
def log_separator3():
    print("# " * 30)
def log_separator4():
    print("* " * 30)


# 测试函数
#__name__：Python中内置变量，表示的当前模块的名字（直接运行当前模块，__name__的值为"__main__"；当该模块被导入时，__name__的值就是模块名

#执行当前文件，则会执行如下代码；如果被当做模块导入，如下代码不执行；
if __name__ == '__main__':
     log_separator1()