"""
多继承：一个子类继承了多个父类
"""


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

# MRO: IMethod Resolution Order
# 注意：当一个类继承了多个父类时，默认优先使用第一个父类中的同名属性或方法，可以使用类名.__mro__属性 或 类名.mro(）方法查看调用顺序。
class HuaweiAiDriving:
    def __init__(self,version='V1.0'):
        self.version = version

    def run(self):
        print(f"使用华为AI智能驾驶系统 {self.brand} {self.model} {self.version} 正在行驶 !!!!!")



class WenJieCar(Car,HuaweiAiDriving):
    def __init__(self,brand,model,color,owner,version='V1.0'):
        Car.__init__(self,brand,model,color,owner)
        HuaweiAiDriving.__init__(self,version)

    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)




if __name__ == '__main__':
    c = WenJieCar('问界',model="M9",color='yellow',owner='ryan',version='V1.1')
    print(WenJieCar.__mro__)
    c.start()

    print(c.__dict__)

    c.run()