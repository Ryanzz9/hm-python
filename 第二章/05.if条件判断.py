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



## if...elif...else 案例

# 根据用户输入的数字，判断数字是正数，还是负数，还是0

#
# num = int(input("请输入数字："))
#
# if num > 0:
#     print(f"{num}是一个正数")
# elif num < 0:
#     print(f"{num}是一个负数")
# else:
#     print(f"{num}是0")



## 完成如下需求
## 1.根据输入用户名、密码进行登录系统。

#- 用户名、密码为 admin/666888 或root/547527 或 zhangsan/123456，则输出登录成功
# - 否则就提示用户名或密码错误

# username = input("请输入用户名：")
# password = input("请输入密码：")
#
# if username == "admin" and password == "666888":
#     print(f"{username} 登录成功")
#
# elif username == "root" and password == "547527":
#     print(f"{username} 登录成功")
# elif username == "zhangsan" and password == "123456":
#     print(f"{username} 登录成功")
#
# else:
#     print(f"用户 {username} 登录失败，用户名或密码错误")

## 练习

## 1. 根据输入的考试成绩，判断成绩等级。

# 大于等于85分为优秀
#60-85分为及格
#否则就是不及格

# score = int(input("请输入成绩："))
#
# if score > 85:
#     print("优秀")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")



## 2. 购物折扣计算：根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。

# 金额 >= 500：8折
#  300 <= 金额< 500：9折
#  100 <= 金额 < 300：95折
#  金额 < 100：无折扣

# amount = int(input("输入商品总额："))
# original = amount
#
# if amount >= 500:
#     amount *= 0.8
#     discount = original - amount
#     print(f"商品总额8折，折扣完{amount:.2f}元，优惠了{discount:.2f}元")
# elif amount >= 300:
#     amount *= 0.9
#     discount = original - amount
#     print(f"商品总额9折，折扣完{amount:.2f}元，优惠了{discount:.2f}元")
# elif amount >= 100:
#     amount *= 0.95
#     discount = original - amount
#     print(f"商品总额95折，折扣完{amount:.2f}元，优惠了{discount:.2f}元")
# else:
#     print(f"无折扣，{amount:.2f}元")

# :.2f 是 Python 中格式化字符串的用法，用于控制数字的显示格式。
#f → fixed-point，表示浮点数格式
#.2 → 表示保留2位小数
#: → 分隔符，前面是变量，后面是格式说明




"""
案例 完成如下需求
三角形类型判断：根据输入的三个边的边长（正整数），判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角形。
构成三角形的条件：两边之和大于第三边

三角形判定规则：
三个边都相等：等边三角形
两个边相等：等腰三角形
三个边都不相等：普通三角形
"""

#
# a = int(input("请输入第一个边的边长："))
#
# b = int(input("请输入第二个边的边长："))
#
# c = int(input("请输入第三个边的边长："))
#
#
# if a + b > c and a + c > b and b + c > a:
#     if a == b and c == b:
#         print(f"a={a},b={b},c={c} 这三个边长能构成等边三角形！！！")
#     elif a == b or c == b:
#         print(f"a={a},b={b},c={c} 这三个边长能构成等腰三角形！！！")
#     else:
#         print(f"a={a},b={b},c={c} 这三个边长能构成普通三角形！！！")
# else:
#     print(f"a={a},b={b},c={c} 这三个边长不能构成三角形！！！")



# 练习：北京市居民年度用电电费计算：根据输入的用电度数，计算电费

# 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
#
# 阶梯电价规则：
#
# 第一档：2880度以下，电费单价0.4883元/度
#
# 第二档：2880-4800度，电费单价0.5383元/度
#
# 第三档：4800度以上，电费单价0.7883元/度



e_usage = int(input("请输入您的用电度数："))
first_gear = 2880 * 0.4883
second_gear = (4800 - 2880) * 0.5383

if e_usage > 4800:
    #e_usage -= 4800 * 0.7883
    e_usage = (e_usage - 4800) * 0.7883
    e_bill = first_gear + second_gear + e_usage
    print(f"当前用电量处于最高档，您的电费为 {e_bill:.4f}")

elif 2880 <= e_usage <= 4800:
    e_usage = (e_usage - 2880) * 0.5383
    e_bill= first_gear + e_usage
    print(f"当前用电量处于二档，您的电费为 {e_bill:.4f}")

else:
    e_bill = e_usage * 0.4883
    print(f"当前用电量处于一档，您的电费为 {e_bill:.4f} 元")