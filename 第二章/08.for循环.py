# for 循环： 遍历输入的字符串

msg = input("请输入需要遍历的字符串：")

for s in msg:
    print(f"元素：{s}")
else:
    print("遍历结束!")


## 案例
#1.计算1-100之间所有奇数之和。 range(1,101)

total1 = 0

# 原始
for i in range(1,101):
    if i % 2 == 1:
        total1 += i
print("1-100之间的奇数累加之和：",total1)

# 简化
for i in range(1,101,2):
    total1 += i
print("1-100之间的奇数累加之和：",total1)



#2.计算100-500之间所有3的倍数的数字之和。range(100,501)

total2 = 0

for i in range(100,501):
    if i % 3 == 0:
       total2 += i
print("100-500之间的数字累加之和：",total2)
