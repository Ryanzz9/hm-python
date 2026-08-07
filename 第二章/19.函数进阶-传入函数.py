# 函数的参数类型


# 加

def add(x,y):
    return x+y

# 减
def sub(x,y):
    return x-y
# 乘
def mul(x,y):
    return x*y
# 除
def div(x,y):
    return x/y




def calc(x,y,oper):
    return oper(x,y)


print(calc(1,2,add))
print(calc(1,2,sub))
print(calc(1,2,mul))
print(calc(1,2,div))



# 匿名函数

# 需求1：打印一个分割线
# 使用 lambda 定义（你原来代码里的 # 井print 应该是打字笔误，不必在意）
out_line = lambda: print("-" * 30)  # 改成了打印30个"-"，分割线更明显
out_line()  # 调用执行打印

# 需求2：计算两个数之和
# 使用 lambda 实现
add = lambda x, y: x + y
result = add(10, 20)
print(f"10 + 20 的结果是: {result}")

# 也可以直接在调用时传参
print(lambda x, y: x + y(3, 5)) # 注意：这行代码会打印函数对象，要加括号调用。正确的是：
print((lambda x, y: x + y)(3, 5)) # 直接调用匿名函数计算 3+5，输出 8

# #需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
data_list =["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]

print(data_list)

data_list.sort(key=lambda item : len(item), reverse=True)
print(data_list)



# 案例1
# 定义一个函数，根据传入的数字，计算该数字阶乘的结果。
# 递归调用，指的是在函数中自己调用自己的情况 ，一定得有终结点(先层层递进，再层层回归 )
"""
jc(10) = 10 * jc(9)
jc(9) = 9 * jc(8)
jc(8) = 8 * jc(7)
jc(7) = 7 * jc(6)
jc(6) = 6 * jc(5)
jc(5) = 5 * jc(4)
jc(4) = 4 * jc(3)
jc(3) = 3 * jc(2)
jc(2) = 2 * jc(1)
jc(1) = 1
"""


def calc(n):
    if n <= 1:
        return 1
    return n * calc(n-1)

print(calc(3))



## 案例2

"""
定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。

具体规则如下：
- 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
- 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""

