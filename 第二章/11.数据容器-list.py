# 列表操作
# 定义列表 -list
s = [56,90,88,65,"A","Hello",True]

print(type(s))

# 访问列表元素

# 获取

print(s[0]) # 正向索引从0开始
print(s[-7]) # 反向索引从-1开始

# 修改

s[5] = "ABC"

print(s)
# 注意:如果指定的索引，超出范围，将会报错 list assignment index out of range
#s[10] = "DEF"
#print(s)

# 删除

del s[6]
print(s)


# 遍历

for item in s:
    print(item)


##切片

# 定义列表
s = ["A","C","H","K","L","B","D","X","C","U"]

# 切片操作 s[开始索引：结束索引：步长]

print(s[0:5:1])
print(type(s[0:5:1]))

print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[:5:2])



## 列表 list 常用方法

# 定义列表

s = [56,90,88,65,90,100,209,72,145]
print(s)

# append():在列表尾部追加元素
s.append(188)
print(s)


# insert() 在指定索引之前，插入元素

s.insert(2,80)
print(s)

# remove() 移除列表第一个匹配的元素

s.remove(90)
print(s)

# pop() 删除列表中指定索引位置的元素并返回（如果未指定，默认删除最后一个）
e = s.pop(1)
print(e)

e = s.pop()
print(e)

print(s)


# sort() 排序

s.sort()
print(s)


# reverse() 反转列表元素
s.reverse()
print(s)



#------------------------------列表 list 案例-------------------------------

# 1.将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。

# 1.定义列表

num_list = []

# 2.将用户输入的10个数字存入列表

for i in range(10):
    num = int(input("请输入一个有效数字："))
    num_list.append(num)

print("数字列表：",num_list)
#
#
# # 3.排序
#
num_list.sort()
print("排序后的数字列表：",num_list)

# 4.输出其中最大值、最小值、平均值。 sum()求和 ； len()获取元素的个数（列表长度）

print("最小值",num_list[0])
print("最大值",num_list[-1])
print("平均值",sum(num_list) / len(num_list))



#2.合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。

num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# # 1.合并列表
# for num in num_list2:
#     num_list1.append(num)
#
# print("合并后的原始列表：",num_list1)
#
# # 2.去重
#
# # 去除重复后的列表
# new_list = []
#
# for num in num_list1:
#     # 判断new_list中是否存在num元素，如果不存在再添加。
#     if num not in new_list: # 判断元素是否存在于列表中，如果存在则返回true，不存在返回false
#        new_list.append(num)
#
# print("去重后的列表：",new_list)

## 简化1 解包

# 解包：将列表这一类的容器解开成一个一个独立的元素
# 组包：将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]
# print("合并后的原始列表：",num_list)

# 2.去重

# 去除重复后的列表
new_list = []

for num in num_list:
    # 判断new_list中是否存在num元素，如果不存在再添加。
    if num not in new_list: # 判断元素是否存在于列表中，如果存在则返回true，不存在返回false
       new_list.append(num)

print("去重后的列表：",new_list)

##简化2
# 1.合并列表
#
num_list = num_list1 + num_list2
#
print("合并后的原始列表：",num_list)
#
# # 2.去重
#
# # 去除重复后的列表
new_list = []

for num in num_list:
    # 判断new_list中是否存在num元素，如果不存在再添加。
    if num not in new_list: # 判断元素是否存在于列表中，如果存在则返回true，不存在返回false
       new_list.append(num)

print("去重后的列表：",new_list)




# 案例3： 生成1-20的平方列表。 ---> range(1,21)
# 方式一：传统方式
num_list = []
for i in range(1,21):
    num_list.append(i**2)

print(num_list)

# 方式二：列表推导式 ——> 就是按照一定的规则快速生成一个列表的方法。语法格式：[要插入的值 for i in 序列/列表]

num_list2 = [ i**2 for i in range(1,21)]

print(num_list2)


# 案例4： 从一个数字列表中提取所有的偶数，并计算其平方，组成一个新的列表。

num_list = [12,32,45,77,80,92,33,57,97,98,110,111,122]

new_list = []

for item in (num_list):
    if item % 2 == 0:
       new_list.append(item**2)

print(new_list)


# 列表推导式语法格式2 ：
#[要插入的值 for i in 序列/列表 if 条件]

num_list = [12,32,45,77,80,92,33,57,97,98,110,111,122]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)




#--------------------------练习----------------------------#

# 1. 将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。
#
#
# 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']

row_list = [*list1, *list2, *list3]

print("去重前原始列表:",row_list)

new_list = []
for i in row_list:
    if i not in new_list:
        new_list.append(i)
    else:
        print(f"{i}重复了", i)
new_list.sort()
print("去重排序后列表:",new_list)



# 将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
print(new_list)


# 将如下列表中的正数提取出来，封装为一个新的列表。
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

new_list = [i for i in list1 if i >0]

print(new_list)

