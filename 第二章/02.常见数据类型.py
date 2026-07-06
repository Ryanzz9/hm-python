# # # 常见数据类型
# # # type() 获取指定的字面量或变量的类型
# #
# # print("Hello")
# #
# # print(type(10)) # int
# # print(type(3.14))# float
# # print(type(True)) #bool
# # print(type(False)) # bool
# # print(type(None)) # NoneType
# #
# # num = -100
# # print(type(num)) # int
# #
# #
# # # isinstance(数据，类型) ——> bool值 ——> 判定数据是否是指定的类型，如果是True ，否则：False
# #
# # print(isinstance(num,int))
# # print(isinstance(num,float))
# # print(isinstance(num,bool))
# #
# #
# # # 字符串
# # # 定义字符串的三种方式
# #
# # s1 = "hello"
# # s2 = 'world'
# # s3 = """
# # hello:
# #     python!!!!!!
# #     assssss@@@@@
# # """
# # # 三引号定义（多行字符串）
# #
# # print(s1)
# # print(s2)
# # print(s3)
# #
# #
# # # 定义字符串 ---> It's very good
# # # 转义字符
# # msg = 'It\'s very good'
# #
# # print(msg)
# #
# #
# # msg2 = "It's very good"
# #
# # print(msg2)
# #
# #
# # msg3 = 'hello 的意思是"您好"'
# # print(msg3)
# #
# #
# # print("\taaaaaaaaaaaaaaaa\n\tbbbbbbbbbb") #\n 缓缓 \t 按了tab
# #
# from tkinter.font import names
#
# ## 字符串的拼接
# s1 = "人生苦短" "我用python" ",OK"
# print(s1)
#
# mss1 = "人生苦短"
# mss2 = "我用python"
#
# print("龟叔说: " + mss1 + "," + mss2)
#
# ## 案例
# # str(int数字) ---> 将int类型的数字转为字符串
# name = "xin"
# age = 18
# pro = "运维"
# hobby = "Python"
# print("大家好,我是" + name + ",今年" + str(age) + "岁,学习的专业是" + pro + ",爱好" + hobby)
#
#
#


# 字符串格式化——> 方式一：%s 占位符

name = "xin"
age = 18
pro = "运维"
hobby = "Python"
print("大家好,我是%s ,今年%s岁,学习的专业是%s,爱好%s" % (name, age, pro, hobby))

# 字符串格式化——> 方式二：f"..{变量名/表达式}"

name = "xin"
age = 18
pro = "运维"
hobby = "Python,java"
print(f"大家好,我是{name} ,今年{age}岁,学习的专业是{pro},爱好{hobby}")
