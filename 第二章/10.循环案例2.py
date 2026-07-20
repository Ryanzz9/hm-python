"""
案例: 猜数字游戏
import random
random_number = random.randint( a: 1, b: 100)

1. 系统随机生成一个随机数
2. 用户根据提示猜数字，并将所猜的数字输入系统
3. 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
4. 如果猜对，系统自动退出，游戏结束
"""

import random

random_num = random.randint(1, 100)
cont = 0

while True:
    try:
        num = int(input("请输入一个数字："))
        cont += 1  # 每次输入都计数

        if num > random_num:
            print("大了")
        elif num < random_num:
            print("小了")
        else:
            print("猜对了 666")
            break
    except ValueError:
        print("请输入有效的数字！")

# 输出结果
if cont > 5:
    print(f"随机生成的数字是：{random_num},一共猜测{cont}次,运气太差!")
elif cont <= 3:
    print(f"随机生成的数字是：{random_num},一共猜测{cont}次,运气太厉害")
else:
    print(f"随机生成的数字是：{random_num},一共猜测{cont}次,运气可以")