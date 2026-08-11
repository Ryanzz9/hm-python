# 1. 基础变量定义（未指定类型注解）
import math

# 变量定义 - 未指定类型注解
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count":2 , "total":10}
goods = ("手机", 6999, 1)


names.append("a")
names.append(1233)


# 2. 进阶变量定义（指定类型注解）
# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count":2 , "total":10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)


phones2.add(123123123)

options2.update({"sxxxxx":"asdasd" , "1233333":"sadasdasd"})

names2.append("asd")






### 函数类型注解

def circle_area_len(r:int)->tuple[float,float]:
    return round(3.14 * r * r,1) ,round(2*3.14 * 4 ,1)

al = circle_area_len(10)
print(al)



def calc_order_cost(*args:tuple[str,float,int],coupon:int=0,score:int=0,express:float=0.0)->float:
    """
    用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param express: 运费信息
    :return:
    """
    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # #1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    #2.扣减优惠券

    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    #3.减扣积分抵扣

    if total_cost >= 5000 and score // 100  <= total_cost:
        total_cost -= score // 100


    #4.添加运费

    total_cost += express

    return total_cost


# 测试




print(calc_order_cost(("4090",18888,3),("5090",29999,10),("5080",15999,4)))

