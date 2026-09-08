class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'duck {self.age} 岁的 {self.name} 正在游泳....')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'dog {self.age} 岁的 {self.name} 正在游泳....')

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self): # 启动
        print(f'pig {self.age} 岁的 {self.name} 正在游泳....')


# 定义一个公共函数
def go_swimming(duck: Duck):  # 3 用法
    duck.swimming()

# 测试代码
if __name__ == '__main__':
    go_swimming(Dog(name="旺财", age=4))
    go_swimming(Duck(name="唐老鸭", age=2))
    go_swimming(Pig(name="佩奇", age=1))