## if 条件判断：如果分数超过680，就去读清华


score = 600

if score > 680:
    print("欢迎你来清华读书")
    print("也恭喜你即将踏入精彩的大学生活")
print("______________________________")

# # if案例：结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现（正确账号和密码为18888888888/666888）
#
#
# ok_account = "188888888"
# ok_account_password = "666888"
#
# # 1. 接收用户输入的账号和密码
#
# account = input("请您输入账号：")
#
# password = input("请您输入密码： ")
#
# # 2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入B站首页
#
# if account == ok_account and password == ok_account_password:
#     print("登录成功~~~")
#     print("进入B站首页~~~")
#
# # 3.判断账号和密码是否有错误的，如果有任何一个错误，则登录失败，提示错误信息
# if account != ok_account or password != ok_account_password:
#     print("登录失败")
#     print("密码或账号错误")

#
# ok_account = "188888888"
# ok_account_password = "666888"
#
# # 1. 接收用户输入的账号和密码
#
# account = input("请您输入账号：")
#
# password = input("请您输入密码： ")
#
# # 2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入B站首页
#
# if account == ok_account and password == ok_account_password:
#     print("登录成功~~~")
#     print("进入B站首页~~~")
# else:
#     print("登录失败")
#     print("密码或账号错误")

## 需求：根据用户输入的年份，判断这一年是闰年还是平年。

# year = int(input("请输入需要判断的年份："))
#
# # 如果是 非整百年份，且能被4整除 就是闰年；整百年份，必须被400整除也是闰年
#
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

#
# 练习 完成如下需求
#
# 需求1：根据用户输入的数字，判断该数字是奇数还是偶数。
#
# num = int(input("请输入需要判断的数字："))
#
# if num % 2 == 0:
#     print(f"{num}:是偶数")
# else:
#     print(f"{num}:是奇数")
#
# 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）。
#
# age = int(input("请输入年龄："))
#
# if age >= 18:
#     print(f"{age}:成年")
# else:
#     print(f"{age}:未成年")
#
# 需求3：根据用户输入的数字，判断该数字是正数还是负数（不考虑0）。
#
# nums = int(input("请输入："))
#
# if nums > 0:
#     print(f"{nums}:正数")
# else:
#     print(f"{nums}:负数")
#
# 需求4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格了）。
# score = int(input("请输入："))
#
# if score > 60:
#     print(f"{score}:及格了")
# else:
#     print(f"{score}:不及格")
