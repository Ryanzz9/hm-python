# 字面量的写法
print(100) # 整数(int)
print(3.14) # 浮点数/小数(float)
print(True)  # 布尔(bool)
print(False) # 布尔(bool)
print("Hello Python") #字符串(str)
print('--------') # 字符串(str)
print(None) # 空值(NoneType)

# 布尔类型本质也是整数类型 (True - 1; False - 0)
print(True + 1 ) # 2
print(False - 1 ) # -1



# 变量 -----> Python 是动态类型语言，一个变量是可以存储不同类型的数据的（但是在项目开发中，推荐变量只存储一种类型的数据）
num = 1114.1
print(num)


num = num + 1

print(num)

num = "ok"

print(num)

num = True
print(num)
num = False
print(num)


# 案例

# 基础播放量

# base = 20.7 # 基础播放量
# incr = 50 # 每一个月新增播放量
# print("未来第一个月的播放总量：",base+incr)
# print("未来第二个月的播放总量：",base+incr+incr)

# 升级： 一次性可以定义多个变量

base,incr = 20.7,50

print("未来第一个月的播放总量：",base+incr)
print("未来第二个月的播放总量：",base+incr+incr)


# ctrl + d 复制一行



# 标识符
true = 1
print(true)


#案例1 ： 现有两个变量，分别为 a=10 ，b = 20 ,现在需要将这两个变量值交换，然后输出到控制台。
#
# a = 10
# b = 20
#
# c = a # c=10
# a = b # a =20
# b = c # b =10
# print(a)
# print(b)


# 练习 完成如下需求
# 现有三个变量，分别为：a = 100，b = 200，c = 300，现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b，并将其输出到控制台。

a = 100
b = 200
c = 300

print(a,b,c)  # 输出：100 200 300

c,a,b = a,b,c  # 将 a,b,c 的值分别赋给 c,a,b

print(a,b,c)  # 输出：200 300 100


# 原来的 a 值 → 赋给 c
#
# 原来的 b 值 → 赋给 a
#
# 原来的 c 值 → 赋给 b







