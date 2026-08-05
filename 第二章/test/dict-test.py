"""
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5. 退出购物车
"""
menu = """
########## 购物车系统 ##########
#         1. 添加购物车        #
#         2. 修改购物车        #
#         3. 删除购物车        #
#         4. 查询购物车        #
#         5. 退出购物车        #
########## 购物车系统 ##########
"""

# 1.制作菜单
print("欢迎使用购物车管理系统 ~")
print(menu)

shopping_car = {}
while True:

    # gwc = {"4090":{"name":4090,"price":2222,"num":2}}

    # 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。

    choice = int(input("请输入具体功能:"))

    match choice:
        case 1:
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            if goods_name in shopping_car:
                print("商品已存在请重新输入")
            else:
                shopping_car[goods_name] = {"name": goods_name, "price": goods_price, "num": goods_num}
                print("商品添加成功")
        case 2:
            # 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
            goods_name = input("请输入要修改的购物车商品名称：")
            if goods_name not in shopping_car:
                print("商品不存在，请重新输入")
                # continue
            else:
                goods_price = float(input("请输入商品价格："))
                goods_num = int(input("请输入商品数量："))
                shopping_car[goods_name] = {"name": goods_name, "price": goods_price, "num": goods_num}
                print("修改商品信息成功")
        case 3:
            # 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
            goods_name = input("请输入要删除的购物车商品名称：")
            if goods_name not in shopping_car:
                print("该商品不存在,请重新输入")
            else:
                del shopping_car[goods_name]
                print("商品删除成功")
        case 4:
            # 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
            for goods_name in shopping_car.keys():
                goods_info = shopping_car[goods_name]
                print(f"商品名称：{goods_info["name"]},商品价格：{goods_info["price"]},商品数量：{goods_info["num"]}")

        case 5:
            print("系统退出")
            break
        case _:
            print("非法输入")



#
# car = {
#     "4090":{"name":"4090","price":14333,"num":2},
#     "4080":{"name":"4080","price":8333,"num":3}
# }
#
#
# for goods_name in car.keys():
#     #car.keys() 返回一个由所有键组成的视图（"4090", "4080"）。每次循环，将当前键赋值给 goods_name
#     print(goods_name) # 通过 car[goods_name] 获取对应的内部字典，并赋值给 goods_info
#     goods_info = car[goods_name]
#     # 使用 f-string 格式化字符串，输出商品信息。
#     print(f"商品名称：{goods_info["name"]},商品价格：{goods_info["price"]},商品数量：{goods_info["num"]}")
#
#
#
# print()
# print()
#
# # 用 items() 同时获取键和值
#
#
# for key, goods_info in car.items():
#     print(key,goods_info)
#     print(f"商品名称：{goods_info['name']},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
#
#
# car = {
#     "4090": {"price": 14333, "num": 2},
#     "4080": {"price": 8333, "num": 3}
# }
#
# for model, info in car.items():
#     print(f"商品名称：{model},商品价格：{info['price']},商品数量：{info['num']}")