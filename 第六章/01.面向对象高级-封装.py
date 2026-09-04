"""
封装：将数据(属性)和操作数据的方法绑定在一起，形成一个独立的单元(类)，保护数据不被外部访问，通过访问修饰符实现封装。
     1.私有属性：在属性名前加双下划线__
     2.私有方法：在方法名前加双下划线__

"""

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner # 拥有者(私有属性)

    def start(self):
        print(f"{self.brand} {self.model} start !!!!!")

    def run(self):
        print(f"{self.__owner},{self.brand} {self.model} run!!!!!!!") # 调用私有方法
        self.__control_fuel()

    def stop(self):
        print(f"{self.brand} {self.model}  stop !!!!!")

    def __control_fuel(self):# 私有方法
        print(f"{self.brand} {self.model} control fuel !!!!!")

    def get_owner(self):
        return self.__owner[0:1] + "******"


if __name__ == '__main__':
    car = Car('audi',model="a6",color='yellow',owner='ryan')
    print(car.model)
    print(car.brand)
    print(car.color)
    #print(car.__owner)

    car.start()
    car.run()
    car.stop()
    #car.__control_fuel()
    print(car.get_owner()) # 通过公共方法调用私有属性

    #注意事项：Python中是没有真正的私有机制；
    print(car._Car__owner)
    car._Car__control_fuel()
