#支付商品功能

"""
goods = [
    {'goods_id':1,'goods_name':'苹果','goods_price':5.0},
    {'goods_id':2,'goods_name':'香蕉','goods_price':3.0},
    {'goods_id':3,'goods_name':'牛奶','goods_price':8.0},
    {'goods_id':4,'goods_name':'面包','goods_price':6.0},
    {'goods_id':5,'goods_name':'巧克力','goods_price':10.0},

]
"""


def pay_cart(cart_goods):
    sum_price = 0.0  # 总价
    for goods_part in cart_goods:
        sum_price += goods_part['goods_price']
    print("总价为：{}".format(sum_price))
