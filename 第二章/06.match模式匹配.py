# match...case 模式匹配: 工作日程安排

day = input("请输入星期(1-7): ")

match day:
    case "1":
        print("周一：工作会议日")
    case "2":
        print("周二：学习培训日")
    case "3":
        print("周三：项目开发日")
    case "4":
        print("周四：代码审查日")
    case "5":
        print("周五：总结规划日")
    case "6" | "7":
        print("周末：休息休息")
    case _:
        print("输入错误！！")


## 案例：基于match...case 实现一个简易的计算器，可以实现 + - * / 运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。

num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
oper = input("请输入运算符，+ - * /")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 !=0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持")


## 练习 简单游戏指令系统

#请你编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作（输出控制台）。


goper = input("请输入指令:")

match goper:
    case "上" | "w" | "W":
        print("	角色向上移动")
    case "下" | "s" | "S":
        print("	角色向下移动")
    case "左" | "a" | "A":
        print("	角色向左移动")
    case "右" | "d" | "D":
        print("	角色向右移动")
    case "跳" | "" | " ":
        print("	角色跳跃")
    case "攻击" | "j" | "J":
        print("	角色发起攻击")
    case "退出" | "esc" | "ESC":
        print("	角色退出游戏")
    case _:
        print("输入错误！")