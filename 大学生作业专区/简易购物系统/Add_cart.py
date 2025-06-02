#增添商品功能
from time import sleep

from Pay_cart import *

from Cart_Display import *

from Input_goods import *
"""
goods = [
    {'goods_id':1,'goods_name':'苹果','goods_price':5.0},
    {'goods_id':2,'goods_name':'香蕉','goods_price':3.0},
    {'goods_id':3,'goods_name':'牛奶','goods_price':8.0},
    {'goods_id':4,'goods_name':'面包','goods_price':6.0},
    {'goods_id':5,'goods_name':'巧克力','goods_price':10.0},

]
"""
def add_cart(cart_goods,goods):
    input_goods(goods)  #打印商品列表
    
    news_cart_goods = int(input("请输入您想添加的商品编号："))
    found = False
    for goods_part in goods:
        if news_cart_goods == goods_part['goods_id']:
            cart_goods.append(goods_part)
            found = True
            break
    if found:
        cart_display(cart_goods)
        pay_cart(cart_goods)
    else:
        print(f"未找到编号为{news_cart_goods}的商品，请检查商品编号！")

    #判断用户是否继续添加商品

    next = input("是否继续添加商品？(y(enter)/n)")

    if next == 'y' or next == 'Y' or next == '':
        return add_cart(cart_goods,goods)
    else:
        print("您当前的购物商品为： ")
        for cart_goods_part in cart_goods:
            print("商品编号：{} 商品名称：{} 商品单价：{}"\
                .format(cart_goods_part['goods_id'],cart_goods_part['goods_name'],\
                cart_goods_part['goods_price']))



    """
    想修改一下系统，帮助客户自动跳转付费界面。
    """

    result = input("是否跳转到付费界面？(y(enter)/n)")
    if result == 'y' or result == 'Y' or result == '':
        print("跳转到付费界面......")
        sleep(1)
        pay_cart(cart_goods)
        return True
    else:
        print("您有一笔购物订单，请及时支付！")
        return False



