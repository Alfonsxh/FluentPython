#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 11-04-Tombola.py
@time: 18-4-18 下午10:21
@version: v1.0
"""

"""
实现一个随机器，不重复输出里面的内容。类似于宾果机和彩票机。
"""

import abc
import random


# from collections import abc   # 包含了很多个抽象基类，具体 Ctrl + 鼠标左键


class Tombola(abc.ABC):
    @abc.abstractmethod  # abstractmethod必须放在最里层
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，并将结果返回"""

    def loaded(self):
        """如果元素个数大于等于1，返回True，否则返回False"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个由当前元素构成的有序元祖"""
        items = []
        while True:
            try:
                items.append(self.pick())  # 先从中读取所有的元素
            except:
                break
        self.load(items)  # 再将其存放回去
        return tuple(items)


# -----------------------------------------BingoCage-------------------------------
class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


def lenBingo(cls):
    return len(cls._items)


def getitem(cls, position):
    return cls._items[position]


def setitem(cls, position, card):
    cls._items[position] = card


def repr(cls):
    return str(cls._items)


print("Before:", BingoCage.__dict__)

BingoCage.__len__ = lenBingo
BingoCage.__setitem__ = setitem
BingoCage.__getitem__ = getitem
BingoCage.__repr__ = repr

print("After:", BingoCage.__dict__)

bingo = BingoCage([1, 2, 3, 4, 5])
print("Before:", bingo)
random.shuffle(bingo)
print("After random.shuffle(bingo)", bingo)


# -----------------------------------------LotteryBlower-------------------------------
class LotteryBlower(Tombola):
    def __init__(self, items):
        self._balls = list(items)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


lotter = LotteryBlower(range(10))


# ----------------------------------------虚拟子类-------------------------------------------
@Tombola.register  # 将TombolaList注册为Tombola的虚拟子类
class TombolaList(list):
    def pick(self):
        if self:  # 继承list的__bool__方法
            position = random.randrange(len(self))
            return self.pop(position)  # 继承list的pop方法
        else:
            raise LookupError('pick from empty TombolaList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


tombola = TombolaList()

print("issubclass(TombolaList, Tombola):", issubclass(TombolaList, Tombola))  # TombolaList是Tombola的子类
print("isinstance(TombolaList, Tombola):", isinstance(tombola, Tombola))  # tombola是Tombola对象的实例
print("TombolaList.__mro__:", TombolaList.__mro__)  # TombolaList的父类中没有Tombola
print(TombolaList.__dict__)
