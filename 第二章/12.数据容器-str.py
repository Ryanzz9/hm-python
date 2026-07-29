## 字符串 基本操作----》不可变（无法修改）,有序性、可迭代性

s = "Hello World"

print(s[4])
print(s[-8])

for i in s:
    print(i)


## 切片

print(s[0:5:1])
print(s[:5:1])
print(s[0:5])
print(s[:5:])
print(s[0:5])


print(s[6:12:1])
print(s[6:12])
print(s[6::1])


#步长-->正数：从前往后截取；负数：从后往前截取
print(s[-1:-7:-1])
print(s[::-1])



print("---------------------------------------字符串常用方法---------------------------------------")

s = "  Hello-Python-Hello-World  "


#find()查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)


# count()统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)


# replace()将字符串中的指定子串替换为新的内容

sr = s.replace( "-","_")
print(sr)


# upper() 转为大写

su = s.upper()
print(su)

# lower() 转为小写
lu = s.lower()
print(lu)


# 去除字符串两端的空格

ss = s.strip()
print(ss)

#startswith() / endswith() 判断字符串是否是以指定的字符串开头 /结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))


print("---------------------------------------")
print(s)

## 经过以上各种操作后原始字符串没有变化


## 案例
#案例1：邮箱格式验证：户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出”邮箱格式正确”，否则输出”邮箱格式错误”。
email = input("请输入邮箱地址:")

if email.count("@") == 1 and email.count(".") >= 1:
    print(f"{email}邮箱格式正确")
else:
    print(f"{email}邮箱格式错误")


## 方式2 in 运算符，判断子串是否存在字符串中，存在，返回True；否则，返回False

email = input("请输入邮箱地址:")

if email.count("@") == 1 and "." in email:
    print(f"{email}邮箱格式正确")
else:
    print(f"{email}邮箱格式错误")



## 输入一个字符串，判断该字符串是否是回文(两边对称)。
##黄山落叶松叶落山黄
##上海自来水来自海上


str1 = input("请输入字符串:")

if str1[0] == str1[-1]:
    print(f"{str1} 是回文")
else:
    print(f"{str1} 不是回文")



## 将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。

# 存储最终结果的列表
result = []

# 循环10次，接收10个字符串
for i in range(10):
    str2 = input(f"请输入第{i+1}个文字:")
    str3 = str2[::-1]      # 反转
    ustr = str3.upper()    # 转大写
    result.append(ustr)    # 存入列表

# 遍历输出列表内容
for item in result:
    print(item)