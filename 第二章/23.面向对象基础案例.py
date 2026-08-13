## 案例

"""
案例
采用面向对象编程思想完成如下需求
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
5. 展示全部学生成绩：展示出系统中所有学生的成绩
"""

"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加)
1.3 验证成绩范围（0-100分）
1.4 创建学生对象并添加到系统
2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
12.1 输入要修改的学生姓名
2.2 根据姓名查找该学生，显示该生当前成绩信息
2.3 输入新的语文、数学、英语成绩
2.4 更新学生成绩数据
3.删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4.查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
4.1输出格式为："姓名：张三语文：85数学：90英语：88总分：263"
5. 展示全部学生成绩：展示出系统中所有学生的成绩
"""

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



if __name__ == '__main__':
   zx = Student("张山",67,87,78)
   print(zx)

   zx.update_score(english=89)

   print(zx)