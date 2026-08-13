# 定义类 ----> 不推荐动态的为对象添加属性

class Car:
    pass

c1 = Car()

# 动态的为对象添加属性

c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000

# <__main__.Car object at 0x00000226EB0FB770>  内存地址
print(c1)

# 查看对象属性
# 会将对象中的所有属性以字典的形式输出出来
print(c1.__dict__)

print(c1.color)
print(c1.brand)
print(c1.name)



# 定义类

class Cars:
    # __init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性；
    # self : 是第一个参数，表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类型的对象初始化完毕，对象属性已经添加完毕!!!")


# 创建对象

c2 = Cars(c_color="red",
          c_brand="BMW",
          c_name="X7",
          c_price=800000)

print(c2.__dict__)


c3 = Cars(c_color="blue",
          c_brand="BMW",
          c_name="X3",
          c_price=300000)

print(c3.__dict__)



## 定义类 -实例方法

class Cars:
    # __init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性；
    # self : 是第一个参数，表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类型的对象初始化完毕，对象属性已经添加完毕!!!")

    def running(self):
        print(f"{self.name},{self.brand},正在高速行驶")


    def total_price(self,discount,rate=0.3):
        """
        计算提车的总费用，包含两个部分：车的价格，税费
        :param discount:折扣
        :param rate:税率
        :return:提车总费用
        """
        total_price = self.price * discount + rate * self.price
        return total_price
     #魔法方法
    def __str__(self):
        return f"{self.name} {self.brand} {self.price} {self.color}"

    def __eq__(self, other):
        return self.price == other.price and self.color == other.color and self.name == other.name and self.brand == other.brand

    def __lt__(self, other):
        return self.price < other.price

# 测试

c3 = Cars(c_color="red",
          c_brand="BMW",
          c_name="X7",
          c_price=800000
)

c3.running()

print(c3.total_price(discount=0.9))

c4 = Cars(c_color="yellow",
          c_brand="理想",
          c_name="i6",
          c_price=250000
)

c4.running()

print(c4.total_price(discount=0.9))



c5 = Cars(c_color="yellow",
          c_brand="理想",
          c_name="i6",
          c_price=250000
)

c5.running()

print(c5.total_price(discount=0.9))








# 默认不支持比较大小
print(c3)
print(c4)
print(c5)
#<__main__.Cars object at 0x000002F036484EC0>
#<__main__.Cars object at 0x000002F03465D310>
print(c4 == c5)

#False
print(c3 > c4)
# TypeError: '<' not supported between instances of 'Car' and 'Car'


####实例属性与类属性



class Cars:
    # 类属性（所有实例对象共享）
    wheel = 4 # 轮胎数量
    tax_rate = 0.1 # 购置税率
    # __init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性；
    # self : 是第一个参数，表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        # 实例属性优先级高。#通过实例对象，查找属性时，会先查找实例属性；实例属性不存在，再查找类属性
        self.wheel = 2
        print("Car类型的对象初始化完毕，对象属性已经添加完毕!!!")

    def running(self):
        print(f"{self.name},{self.brand},正在高速行驶")


    def total_price(self,discount,rate=0.3):
        """
        计算提车的总费用，包含两个部分：车的价格，税费
        :param discount:折扣
        :param rate:税率
        :return:提车总费用
        """
        total_price = self.price * discount + rate * self.price
        return total_price


s1 = Cars("白色","BYD","宋",178000)

print(s1.brand)
print(s1.name)
print(s1.price)
print(s1.wheel)
print(s1.tax_rate)

##通过类名访问类属性
print(Cars.wheel)
print(Cars.tax_rate)

s2 = Cars("黑色","Tesla","Model Y",268000)




