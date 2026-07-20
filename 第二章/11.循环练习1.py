"""
**练习:** 完成如下需求
需求1：将1-1000之间（含1000)所有的5的倍数的数字累加起来。

需求2：统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"字符串中有多少个a和k。
"""
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print("所有的5的倍数的数字累加:",total)


a = 0
k = 0
rstr = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"

for char in (rstr):
    if char == "k":
        k = k + 1
    elif char == "a":
        a = a + 1
print(f"a出现{a}次,k出现{k}次")


rstr = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
a = rstr.count("a")
k = rstr.count("k")
print(f"a出现{a}次,k出现{k}次")