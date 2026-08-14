"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5. 退出购物车
"""


class ShoppingCart:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"商品名称{self.name} 商品价格 {self.price} 商品数量 {self.quantity}"


    def update_goods(self,price=None,quantity=None):
        if price is not None:
           self.price = price
        if quantity is not None:
           self.quantity = quantity




class ShoppingManagement:
    system_version = "1.0"
    system_name = "购物车管理系统"
    def __init__(self):
        self.shopping_cart_list = []


    #1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。

    def add_shopping_cart(self):
        name = input("请输入商品名称：")
        # 判断商品是否存在，如果存在，则添加失败不能重复添加
        for s in self.shopping_cart_list:
            if s.name == name:
                print("该商品已经存在添加失败")
                return
        price =  int(input("请输入商品价格："))
        quantity = int(input("请输入商品数量："))
        goods = ShoppingCart(name, price, quantity)
        self.shopping_cart_list.append(goods)
        print("商品信息添加成功")

    # 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。

    def update_shopping_cart(self):
        name = input("请输入商品名称：")
        # 判断商品是否存在，如果存在，则添加失败不能重复添加
        for s in self.shopping_cart_list:
            if s.name == name:
               price =  int(input("请输入商品价格："))
               quantity = int(input("请输入商品数量："))
               s.update_goods(price, quantity)
               print("商品信息修改成功")
               return
        print("商品不存在")

    #3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    def remove_shopping_cart(self):
        name = input("请输入商品名称：")
        # 判断商品是否存在，如果存在，则添加失败不能重复添加
        for s in self.shopping_cart_list:
            if s.name == name:
                self.shopping_cart_list.remove(s)
                return
        print("购物车不存在")

    # 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。

    def query_shopping_cart(self):
        for s in self.shopping_cart_list:
            print(s)



    def run_shopping_cart(self):
        print(f"欢迎使用购物车管理系统V{ShoppingManagement.system_version}")

        while True:
            print()
            print("####################################################################")
            print("1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车    5.退出购物车     ###")
            print("####################################################################")

            choice = input("\n请输入要执行的操作1-5：")

            match choice:
                case "1":
                    self.add_shopping_cart()
                case "2":
                    self.update_shopping_cart()
                case "3":
                    self.remove_shopping_cart()
                case "4":
                    self.query_shopping_cart()
                case "5":
                    print("bye")
                    break
                case _:
                    print("非法输入")


if __name__ == "__main__":
    shopping_cart = ShoppingManagement()
    shopping_cart.run_shopping_cart()

