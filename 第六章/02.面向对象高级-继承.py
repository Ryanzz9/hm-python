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






# 燃油车
class Fuelcar(Car):
    pass

# 电动车
class ElectricCar(Car):
    pass


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
    print(fuelcar.get_owner())


    electriccar = ElectricCar('xiaomi',model="su7",color='blue',owner='ryan')
    print(electriccar.model)
    print(electriccar.brand)
    print(electriccar.color)
    #print(electriccar.__owner)

    electriccar.start()
    electriccar.run()
    electriccar.stop()
    print(electriccar.get_owner())
 
