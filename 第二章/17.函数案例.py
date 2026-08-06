#1.定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积= 底 * 高 /2 ）。
from idlelib import config
from operator import truediv


def triangle_area(b,h):
    """
    根据传入的底和高计算三角形面积的函数（三角形面积= 底 * 高 /2 ）
    :param b: 底
    :param h: 高
    :return:  三角形面积
    """
    return b * h / 2

print("底长为 30,高度为 20的三角形面积:",triangle_area(30,20))



#2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。

def count_aeiou(s):
    """
    统计字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
    :param s:  字符串
    :return: 元音个数
    """
    count = 0
    for z in s:
        if z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u':
            count += 1

    return count


tj = count_aeiou("Hello python Hello python ")

print(f"字符串中元音字母的个数:{tj}")



#3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。

s_list = [588,603,455,477,489,503]

def calc_socre(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)
    :param socre_list: 班级学员高考成绩列表
    :return: 最高分、最低分、平均分(保留1位小数)
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list),1)

    return max_s, min_s, avg_s

c_max ,c_min,c_avg = calc_socre(s_list)


print(f"最高分{c_max},最低分{c_min},平均分{c_avg}")



"""
1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。

- 分数 >= 90:A
- 分数 >= 75:B
- 分数 >= 60:C
- 分数 < 60：D

"""

def calc_level(score):
    """
    根据传入的分数，计算对应的分数等级并返回。
    :param score:分数
    :return:等级
    """
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

score_level = calc_level(50)
score_level = calc_level(99)
print(score_level)

"""
2.定义一个函数，用于判断一个字符串是否是回文串，返回bool值。

- 把字符串反转，如果和原字符串相同，就是回文串。(如:"level","radar","黄山落叶松叶落山黄")
"""

def is_palindrome(s):
    for i in range(len(s) // 2):   # 只遍历前一半
        if s[i] != s[-i-1]:        # 对称位置不相等
            return False
    return True                    # 全部对称位置都相等


print(is_palindrome("level"))   # True
print(is_palindrome("abc"))     # False (i=0时 'a'!='c'，直接返回False)
print(is_palindrome("abca"))    # False (i=0时 'a'=='a'继续，i=1时 'b'!='c'返回False)



# 3.定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。

def clock_cg(c):
    h = c // 3600
    remainder = c % 3600
    m = remainder // 60
    s = remainder % 60

    return h,m,s

h,m,s = clock_cg(3661)

print(h,m,s)

"""
/（浮点数除法）
//（整除 / 地板除）
%（取模 / 取余数）
remainder = total % 3600  # 61（扣掉1小时后，还剩61秒）
minutes = remainder // 60 # 1（完整的1分钟）
seconds = remainder % 60  # 1（最后剩下的1秒）
"""



# 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形）。

def triangle_deter(s1,s2,s3):
    #先判断能否构成三角形
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
       if s1 == s2 == s3:
           return "等边三角形"
       elif s1 == s3 or s2 == s3 or s1 == s2:
           return "等腰三角形"
       else:
           return "普通三角形"
    else:
        return "不能构建三角形"

triangle_type = triangle_deter(20,2,20)

print(triangle_type)

print(triangle_deter(10, 20, 20))  # 等腰三角形
print(triangle_deter(3, 4, 5))     # 普通三角形
print(triangle_deter(2, 2, 2))     # 等边三角形
print(triangle_deter(1, 1, 2))     # 不能构成三角形（1+1 不大于 2）