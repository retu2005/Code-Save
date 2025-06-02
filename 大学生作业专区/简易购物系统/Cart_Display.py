"""
goods = [
    {'goods_id':1,'goods_name':'苹果','goods_price':5.0},
    {'goods_id':2,'goods_name':'香蕉','goods_price':3.0},
    {'goods_id':3,'goods_name':'牛奶','goods_price':8.0},
    {'goods_id':4,'goods_name':'面包','goods_price':6.0},
    {'goods_id':5,'goods_name':'巧克力','goods_price':10.0},

]

"""
from Pay_cart import *


def cart_display(cart_goods):
    if len(cart_goods) == 0:
        print("您的购物车为空！")
        return
    else:
        print("当前您的购物车中有如下商品： ")
    for cart in cart_goods:
        print("商品编号：{} 商品名称：{} 商品单价：{}"\
                .format(cart['goods_id'],cart['goods_name'],\
                cart['goods_price']))

    #print("总价：{} ".format(pay_cart(cart_goods)))

