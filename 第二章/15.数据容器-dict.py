# 字典
# 定义字典 --- key不能重复(如果重复，后面的值，会覆盖前面的值)

dict1 = {"王林":670,"李慕婉":608,"徐立国":580,"韩立":688,"王林":700}

print(dict1)
print(type(dict1))

#key必须得是不可变类型(str，int，float，tuple)，不能是 list、set、dict
#dict2 = {0:670, 1.5:608, (1,2):580, ['A','B']:688}
dict2 = {0:670, 1.5:608, (1,2):580, ('A','B'):688}
print(dict2)


# 访问
print(dict1["王林"])

dict1["李慕婉"] = 688 # 修复
print(dict1)



#------------------------字典 常见操作 ------------------------
dict1 = {"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
print(dict1)

# 添加 - key不存在就是添加

dict1["涛哥"] = 550
print(dict1)


# 修改 -key存在就是修改
dict1["涛哥"] = 700
print(dict1)



# 查询
print(dict1["涛哥"]) # 根据key获取value
print(dict1.get("涛哥")) # 根据key获取value

print(dict1.keys()) # 获取所有的key
print(dict1.values()) # 获取所有的value
print(dict1.items()) # 获取所有的键值对 key:value


# 删除

score = dict1.pop("许立国")

print(score)
print(dict1)

del dict1["韩立"]
print(dict1)


# 遍历

for k in dict1.keys():
    print(f"{k}: {dict1[k]}")


for item in dict1.items():
    print(f"{item[0]}: {item[1]}")

for k,v in dict1.items():
    print(f"{k}: {v}")


"""
字典-案例

开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。

5. 退出购物车
"""
shopping_cart = {}
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

while True:

    choice = input("请选择要执行的操作(1-5)：")

    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            if goods_name in shopping_cart:
                print("该商品已存在,请重新输入")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("添加商品成功")
        case "2":  # 修改购物车
            goods_name = input("请输入要修改商品的名称：")
            # 如果商品不存在，则提示错误信息，重新选择
            if goods_name not in shopping_cart:
                print("该商品不存在,请重新输入")
                continue
            goods_price = float(input("请输入商品最新价格："))
            goods_num = int(input("请输入商品最新数量："))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("修改商品信息成功")
        case "3":  # 删除购物车
            goods_name = input("请输入要删除商品的名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在,请重新输入")
            else:
                del shopping_cart[goods_name]
                print("商品删除成功")
        case "4":  # 查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格：{goods_info["price"]},商品数量{goods_info["num"]}")
        case "5":  # 退出购物车
            print("退出购物车！")
            break
        case _:  # 匹配其他所有情况
            print("非法操作")