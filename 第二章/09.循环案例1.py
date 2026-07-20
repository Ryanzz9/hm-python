"""
需求：根据输入的用户名密码执行登录操作，具体要求如下：

1. 正确的用户名和密码为 `admin/666888`、`zhangsan/123456`、`taoge/888666`
2. 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
3. 输入的用户名和密码不能为空！
4. 登录成功：输出 "登录成功，进入B站首页~"
5. 登录失败：输出 "用户名或密码错误，请重新输入！"

关键字：
    break  只能出现在循环中，表示结束、跳出当前循环（break 跳出循环时后面else中的代码将不会执行）
    continue ：只能出现在循环中，表示中断本次循环，直接进入下一次循环
"""


while True:
    # 1.接收输入的用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 2.校验：输入的用户名和密码不能为空！
    if username == "admin" and password == "":
        print("输入的用户名和密码不能为空！！请重新输入")
        continue # 结束 当前循环直接进入下一轮循环

    # 3.判断用户名和密码的正确性，执行登录操作
    if username == "admin" and password == "666888":
        print("登录成功，进入B站首页~")
        break # 跳出循环
    elif username == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页~")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功，进入B站首页~")
        break
    else:
        print("用户名或密码错误，请重新输入！！")
