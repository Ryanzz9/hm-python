"""
基于现有知识开发一个教务管理系统
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5. 列出所有学生：遍历所有学生信息并输出。
6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
7. 退出系统。
"""

menu = """
##################################################【菜单】#####################################################
# 1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有学生    6.统计班级成绩    7.退出系统    #
#############################################################################################################
"""
stu_info = {}

# 1.制作菜单
print("欢迎使用学生信息管理系统 ~")
print(menu)

while True:

    choice = input("请选择要执行的操作(1-7): ")


    # stu_info = {
    #     "李思":{"name":"李思","chinese":80,"math":85,"english":90}
    # }

    match choice:
        case "1":
            # 1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
            stu_name = input("请输入学生姓名：")
            if stu_name in stu_info:
                print("输入的学生已存在，请重新输入")
            else:
                stu_chinese = float(input("请输入语文成绩:"))
                stu_math = float(input("请输入数学成绩:"))
                stu_english = float(input("请输入英语成绩:"))
                stu_info[stu_name] = {"name": stu_name, "chinese": stu_chinese, "math": stu_math,
                                      "english": stu_english}

                print("学生信息已添加")

        case "2":
            # 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
            stu_name = input("请输入学生姓名：")
            if stu_name not in stu_info:
                print("输入的学生不存在，请重新输入")
            else:
                stu_chinese = float(input("请输入语文成绩:"))
                stu_math = float(input("请输入数学成绩:"))
                stu_english = float(input("请输入英语成绩:"))
                stu_info[stu_name] = {"name": stu_name, "chinese": stu_chinese, "math": stu_math,
                                      "english": stu_english}

                print("学生信息已修改")
        case "3":
            # 3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
            stu_name = input("请输入学生姓名：")
            if stu_name not in stu_info:
                print("输入的学生不存在，请重新输入")
            else:
                del stu_info[stu_name]
                print(f"删除{stu_name}成功")
        case "4":
            # 4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
            stu_name = input("请输入学生姓名：")
            if stu_name not in stu_info.keys():
                print("输入的学生不存在，请重新输入")
            else:
                stu_pinfo = stu_info[stu_name]
                print(f"学生姓名{stu_pinfo["name"]},语文成绩{stu_pinfo["chinese"]},数学成绩{stu_pinfo["math"]},英语成绩{stu_pinfo["english"]}")

        case "5":
            # 5. 列出所有学生：遍历所有学生信息并输出。
            for stus in stu_info.keys():
                all_stus =  stu_info[stus]
                print(f"学生姓名{all_stus["name"]},语文成绩{all_stus["chinese"]},数学成绩{all_stus["math"]},英语成绩{all_stus["english"]}")
        case "6":
            chinese_scores_list = []
            math_scores_list = []
            english_scores_list = []

            chinese_max = -float('inf')
            chinese_min = float('inf')
            chinese_max_names = []
            chinese_min_names = []

            math_max = -float('inf')
            math_min = float('inf')
            math_max_names = []
            math_min_names = []

            english_max = -float('inf')
            english_min = float('inf')
            english_max_names = []
            english_min_names = []

            # 6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、
            for stus in stu_info.keys():
                all_stus =  stu_info[stus]
                chinese_scores = all_stus["chinese"]
                math_scores = all_stus["math"]
                english_scores = all_stus["english"]

                chinese_scores_list.append(all_stus["chinese"])
                math_scores_list.append(all_stus["math"])
                english_scores_list.append(all_stus["english"])
            # 更新语文最高/最低
                if chinese_scores > chinese_max:
                   chinese_max = chinese_scores
                   chinese_max_names = [stus]
                elif chinese_scores == chinese_max:
                     chinese_max_names.append(stus)

                if chinese_scores < chinese_min:
                   chinese_min = chinese_scores
                   chinese_min_names = [stus]
                elif chinese_scores == chinese_min:
                     chinese_min_names.append(stus)
            print(f"语文最高分 {chinese_max}，学员：{', '.join(chinese_max_names)}")
            print(f"语文最低分 {chinese_min}，学员：{', '.join(chinese_min_names)}")
            print(f"语文平均分 {sum(chinese_scores_list) / len(chinese_scores_list):.2f}")

            print(f"语文最高分\t{max(chinese_scores_list)}\t最低分\t{min(chinese_scores_list)}\t平均分\t{sum(chinese_scores_list) / len(chinese_scores_list)}\t总分\t{sum(chinese_scores_list)}")
            print(f"数学最高分\t{max(math_scores_list)}\t最低分\t{min(math_scores_list)}\t平均分\t{sum(math_scores_list) / len(math_scores_list)}\t总分\t{sum(math_scores_list)}")
            print(f"英语最高分\t{max(english_scores_list)}\t最低分\t{min(english_scores_list)}\t平均分\t{sum(english_scores_list) / len(english_scores_list)}\t总分\t{sum(english_scores_list)}")

            # top_chinese = max(stu_info.items(), key=lambda item: item[1]["chinese"])
            # print(f"语文成绩最高分的学生是{top_chinese[0]},分数是{top_chinese[1]["chinese"]}")
            #
            # top_math = max(stu_info.items(),key=lambda item: item[1]["math"])
            # print(f"数学成绩最高分的学生是{top_math[0]},分数是{top_math[1]['math']}")
            #
            # top_english = max(stu_info.items(),key=lambda item: item[1]["english"])
            # print(f"英语成绩最高分的学生是{top_math[0]},分数是{top_math[1]['english']}")



        case "7":
            print("退出系统")
            break
        case _:
            print("非法输入")
            continue