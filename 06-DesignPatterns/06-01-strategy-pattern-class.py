#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 06-01-strategy-pattern-class.py
@time: 18-2-10 下午8:24
@version: v1.0 
"""
# 策略模式-类实现
print("*" * 32 + "策略模式-类实现" + "*" * 32)
from collections import namedtuple

Customer = namedtuple("Customer", "name integration")


class Commodity:
    """不同商品的类，用于记录不同商品的名称、数量、单价，并计算总价"""

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:
    """购买类，用于计算所有商品根据不同策略的结果"""

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.carts = list(cart)
        self.promotion = promotion

    def total(self):
        """总价"""
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.carts)
        return self.__total

    def due(self):
        """打折后的价格"""
        if self.promotion is None:
            return self.total()
        else:
            return self.total() - self.promotion.discount(self)

    def __repr__(self):
        return "<Order total:{:.2f}  due:{:.2f}>".format(self.total(), self.due())


class Promotion:
    def discount(self, order):
        """返回折扣的金额"""


class FirstPromotion(Promotion):  # 第一个具体策略
    """为积分为1000或以上的顾客提供5%折扣"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.integration >= 1000 else 0


class SecondPromotion(Promotion):  # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.carts:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class ThirdPromotion(Promotion):  # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""

    def discount(self, order):
        product_item = {item.name for item in order.carts}
        if len(product_item) >= 10:
            return order.total() * 0.07
        return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [Commodity('banana', 4, .5),
        Commodity('apple', 10, 1.5),
        Commodity('watermellon', 5, 5.0)]

print("""
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [Commodity('banana', 4, .5),
        Commodity('apple', 10, 1.5),
        Commodity('watermellon', 5, 5.0)]""")
print("\n")
print("Order(joe, cart, FirstPromotion()):".rjust(35), Order(joe, cart, FirstPromotion()))
print("Order(joe, cart, SecondPromotion()):".rjust(35), Order(joe, cart, SecondPromotion()))
print("Order(joe, cart, ThirdPromotion()):".rjust(35), Order(joe, cart, ThirdPromotion()))
print("\n")
print("Order(ann, cart, FirstPromotion()):".rjust(35), Order(ann, cart, FirstPromotion()))
print("Order(ann, cart, SecondPromotion()):".rjust(35), Order(ann, cart, SecondPromotion()))
print("Order(ann, cart, ThirdPromotion()):".rjust(35), Order(ann, cart, ThirdPromotion()))

