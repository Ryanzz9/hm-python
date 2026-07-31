# 集合


s1 = {5,3,2,0,9,12,43,64,22,5,0}

print(s1)

print(type(s1))

# 定义空集合

s2 = set()

print(s2)
print(type(s2))



## 常见方法：

# add()  添加元素到集合

s1 = {100,200,300,400,500,600,700,800}
print(s1)

s1.add(1200)

print(s1)


# remove() 删除元素

s1.remove(200)
print(s1)

# pop() 随机删除一个集中中的元素并返回
e = s1.pop()
print(e)
print(s1)


# clear()清空集合

s1.clear()
print(s1)


s2 = {"A","B","C","D","E","X","Y"}
s3 = {"C","E","Y","Z"}
#difference() 求两个交集的差集（存在与第一个集合,但不存在于第二个集合）
print(s2.difference(s3))
print(s3.difference(s2))

# union() 求两个集合的并集
print(s2.union(s3))
print(s3.union(s2))

# intersection 求两个集合的交集
print(s2.intersection(s3))
print(s3.intersection(s2))

print()
print()
print()

## 案例

"""
案例完成如下需求
根据提供的班级学生的选课情况,完成如下需求：

1. 找出同时选修了法语和艺术的学生
2. 找出同时选修了所有四门课程的学生
3. 找出选修了足球,但是没有选修篮球的学生
4. 统计每一个学生选修的课程数量
"""

#选修足球学生名单
football_set = {"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"} #选修篮球学生名单
basketball_set ={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"} #选修法语学生名单
french_set ={"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"} #选修艺术学生名单
art_set = { "遁天","天运子","韩立","虎咆","姜老道","紫灵"}


#1.找出同时选修了 法语 和 艺术 的学生 french_set art_set
# 方式一：交集
fa_set = french_set.intersection(art_set)

print(f"同时选修了 法语 和 艺术 的学生:{fa_set}")

# 方式二：&

fa_set2 = french_set & art_set

print(f"同时选修了 法语 和 艺术 的学生:{fa_set2}")


#2.找出同时选修了所有四门课程的学生工

all_set = football_set & french_set & art_set & basketball_set
print(f"同时选修了四门课程的学生:{all_set}")



#3.找出选修了足球,但是没有选修篮球的学生
fnb_set = football_set.difference(basketball_set)

print(f"同时选修足球没有选修篮球的学生:{fnb_set}")


# 方式二 - 差集
fnb2_set = football_set- basketball_set

print(f"同时选修足球没有选修篮球的学生:{fnb2_set}")

# 方式三 集合推导式 --- 快速构建集合 语法 {要往集合中添加的数据 for s in set1 if 条件}

fnb_set3 ={s for s in football_set if s not in basketball_set}
print(f"同时选修足球没有选修篮球的学生:{fnb_set3}")



print("-----------------------------")

#4.统计每一个学生选修的课程数量

# 4.1 获取到学生名单 -- 并集（）


all_students = art_set.union(french_set,football_set,basketball_set)
print(all_students)


all_students = football_set | basketball_set | french_set | art_set
print(all_students)

#4.2 获取每-个学生选修的课程数量
count = 0

for s in all_students:
    if s in basketball_set:
        count += 1
    if s in football_set:
        count += 1
    if s in art_set:
        count += 1
    if s in french_set:
        count += 1
    print(f"{s} 一共选了{count}门课")
    count = 0


print("=========================")

# 修改后更简洁的写法
# 可以利用 Python 的布尔值求和（True 视为 1）
for s in all_students:
    count = (s in art_set) + (s in french_set) + (s in football_set) + (s in basketball_set)
    print(f"{s} 一共选了{count}门课")



print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
##方式二: 列表

all_list = [*football_set,*basketball_set,*art_set,*french_set]

print(all_list)

for s in all_list:
    print(f"{s} 选修了{all_list.count(s)}门课")
