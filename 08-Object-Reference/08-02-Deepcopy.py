#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 08-02-Deepcopy.py
@time: 18-3-4 上午11:25
@version: v1.0
"""


class Bus:
    def __init__(self, passages=None):
        if passages is None:
            self.passages = []
        else:
            self.passages = list(passages)

    def pick(self, name):
        """乘客上车"""
        self.passages.append(name)

    def drop(self, name):
        """乘客下车"""
        self.passages.reverse(name)


import copy

bus1 = Bus(["Alice", "Tom", "James"])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
bus4 = Bus()

# 浅复制与深复制所有的对象id都不同
print("id(bus1), id(bus2), id(bus3), id(bus4):".rjust(30), id(bus1), id(bus2), id(bus3), id(bus4))

# 浅复制对象内部的成员id相同
print("id(bus1.passages), id(bus2.passages), id(bus3.passages), id(bus4.passages):".rjust(30), id(bus1.passages), id(bus2.passages),
      id(bus3.passages), id(bus4.passages))


class HunterBus:
    def __init__(self, passages=[]):  # 不能给予默认参数为空的列表等
        self.passages = passages        # 此处如果是这样赋值，则所有HunterBus()创建的对象共享passages
        # self.passages = list(passages)

    def pick(self, name):
        """乘客上车"""
        self.passages.append(name)

    def drop(self, name):
        """乘客下车"""
        self.passages.reverse(name)


bus1 = HunterBus(["Alice", "Tome"])
bus1.pick("Job")
print("bus1.passages:".rjust(30), bus1.passages)

bus2 = HunterBus()
bus2.pick("Job")
print("bus2.passages:".rjust(30), bus2.passages)

bus3 = HunterBus()
print("bus3.passages:".rjust(30), bus3.passages)

