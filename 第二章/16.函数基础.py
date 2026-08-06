# 函数定义
# 注意：函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义，后调用；

def out_line():
    print("________________________")

# 函数调用
out_line()
out_line()


## 函数的参数与返回值


# 函数1 计算圆的面积

def circle_area(r):
    area = 3.14 *r ** 2
    return area

print(circle_area(2))


# 函数2 计算长方形的面积 - 长 ，宽


def rectangle(l,w):
    """
    根据长方形的长度和宽度,计算长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形的面积
    """
    area = l * w
    return area

print(rectangle(4,5))

help(rectangle)


# 函数3 计算圆的面积，周长 ---半径 --- 如果返回值有多个，多个返回值之间逗号间隔 --- 多个返回值会封装到元组之中

def circle_area_len(r):
    """
    根据圆的半径，计算圆的面积和周长
    :param r: 半径
    :return: 圆的面积，圆的周长
    """
    return round(3.14 * r ** 2,1) , round(2 * 3.14 * r,1)

al = circle_area_len(10)
print(al)


# 解包
area , len = circle_area_len(10)
print(area)
print(len)


# 函数嵌套调用

def func_a():
    print("a before ...")
    func_b()
    print("a after ...")

def func_b():
    print("b before ...")
    func_c()
    print("b after ...")

def func_c():
    print("c ...")


func_a()
print("函数调用完毕")