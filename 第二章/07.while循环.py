# while 循环：打印10遍 “人生苦短，我用python”

i = 0
while i < 10:
    print(f"第{i}次  人生苦短，我用python")
    i += 1
else:
    print("打完循环结束")


## 案例 : 计算1-100之间所有偶数的累加之和。

total = 0 #记录累加之和
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1-100之间的偶数累加之和为：{total}")
