"""
多态：是指同一个方法，具有不同的形态、行为、表现
"""
from altair import FieldOrDatumDefWithConditionStringFieldDefstring


class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner # 拥有者(私有属性)

    def start(self):
        print(f"{self.brand} {self.model} 启动 !!!!!")

    def run(self):
        print(f"{self.__owner},{self.brand} {self.model} 行驶中!!!!!!!") # 调用私有方法
        self.__control_fuel()

    def stop(self):
        print(f"{self.brand} {self.model}  停止 !!!!!")

    def __control_fuel(self):# 私有方法
        print(f"{self.brand} {self.model} control fuel !!!!!")

    def get_owner(self):
        return self.__owner[0:1] + "******"


    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料 !!!!!")
# 燃油车
class FuelCar(Car):
    def charge(self):
        #方式一：super().方法名()
        #super().charge()

        # 方式二：父类名.方法名(self)
        Car.charge(self)
        print(f"{self.brand} {self.model} 正在加油 !!!!!")

# 电动车
class ElectricCar(Car):
    def charge(self):
        Car.charge(self)
        print(f"{self.brand} {self.model} 正在充电 !!!!!")

#补充燃料函数
def handle_charge(car:Car): # 函数参数类型声明 --- 指定的是父类型
    car.charge()


if __name__ == '__main__':
   handle_charge(FuelCar(brand='audi',model='a6',color='yellow',owner='ryan'))
   handle_charge(ElectricCar(brand='deep',model='s05',color='silvery',owner='ryan'))