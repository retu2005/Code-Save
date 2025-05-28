from Add_cart import *

from Pay_cart import *

from Input_goods import *

from Cart_Display import *
#  选择合适的组合类型  int   str   float


#商品列表
goods = [
    {'goods_id':1,'goods_name':'苹果','goods_price':5.0},
    {'goods_id':2,'goods_name':'香蕉','goods_price':3.0},
    {'goods_id':3,'goods_name':'牛奶','goods_price':8.0},
    {'goods_id':4,'goods_name':'面包','goods_price':6.0},
    {'goods_id':5,'goods_name':'巧克力','goods_price':10.0},

]


#用户购物车
cart_goods = []

"""
用户操作区域，便于交互
"""

print("|********欢迎使用购物系统************|")
print("|********1.查看商品列表**************|")
print("|********2.加入购物车****************|")  
print("|********3.结算购物车****************|")
print("|********4.显示购物车****************|")
print("|********5.清空购物车****************|")
print("|********6.退出系统******************|")



while True:
    choice = int(input("请输入操作序号： "))
    if choice == 1:
        input_goods(goods)
        cart_display(cart_goods)
    elif choice == 2:
        add_cart(cart_goods,goods)
        cart_display(cart_goods)
    elif choice ==3:
        pay_cart(cart_goods)
    elif choice == 4:
        cart_display(cart_goods)
    elif choice == 5:
        cart_goods = []
        print("购物车已清空！")
    elif choice == 6:
        break
    input_slect = input("是否继续操作？(y(enter)/n)：")  #input_slect 判断用户是否继续操作，可以用于提前结束。
    if input_slect == 'n':
        break
    if input_slect == 'y' or input_slect == 'Y' or input_slect == '':
        print("|********欢迎使用购物系统************|")
        print("|********1.查看商品列表**************|")
        print("|********2.加入购物车****************|")  
        print("|********3.结算购物车****************|")
        print("|********4.显示购物车****************|")
        print("|********5.清空购物车****************|")        
        print("|********6.退出系统******************|")


print("|********欢迎下次光临****************|")




