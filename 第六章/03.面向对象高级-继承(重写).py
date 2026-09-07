"""
继承：描述的是两个类之间的关系，子类继承父类，就可以获取到父类中的属性和方法（非私有）

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


    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料 !!!!!")




# 重写是指子类继承父类后，如果父类中的方法不满足需求，可以在子类中重新定义父类中已有的方法（方法名相同），从而用子类的实现替换父类的实现。

# 燃油车
class Fuelcar(Car):
    def charge(self):
        #方式一：super().方法名()
        super().charge()

        # 方式二：父类名.方法名(self)
        Car.charge(self)
        print(f"{self.brand} {self.model} 正在加油 !!!!!")

# 电动车
class ElectricCar(Car):
    def charge(self):
        Car.charge(self)
        print(f"{self.brand} {self.model} 正在充电 !!!!!")


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
    # print(car._Car__owner)
    # car._Car__control_fuel()


    fuelcar = Fuelcar('honda',model="crv",color='white',owner='ryan')
    print(fuelcar.model)
    print(fuelcar.brand)
    print(fuelcar.color)
    #print(fuelcar.__owner)

    fuelcar.start()
    fuelcar.run()
    fuelcar.stop()
    fuelcar.charge()
    print(fuelcar.get_owner())


    electriccar = ElectricCar('xiaomi',model="su7",color='blue',owner='ryan')
    print(electriccar.model)
    print(electriccar.brand)
    print(electriccar.color)
    #print(electriccar.__owner)

    electriccar.start()
    electriccar.run()
    electriccar.stop()
    electriccar.charge()
    print(electriccar.get_owner())

 #在继承体系中，如果父类的方法不能满足需求，就可以在子类中重新定义一个与父类同名的方法，从而用子类自己的实现来替换父类的实现，这个就称之为重写