#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 11-02-FrenchDeck.py
@time: 18-4-18 下午9:35
@version: v1.0 
"""
from collections import namedtuple, MutableSequence
import traceback
from random import shuffle

Card = namedtuple("Card", ["rank", "suit"])


# FrenchDeck2，collections.MutableSequence的子类
class FrenchDeck2(MutableSequence):  # 继承抽象基类时，必须实现基类的抽象方法！！
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()  # 4种花色

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]

    # Python魔术方法：http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    #
    # def __setitem__(self, position, card):
    #     self._cards[position] = card

    def __delitem__(self, position):
        del self._cards[position]


try:
    deck2 = FrenchDeck2()
    shuffle(deck2)
    print("deck2 init success!")
except:
    traceback.print_exc()  # 提示，缺少相关方法的实现


def setitem(deck, position, card):
    deck._cards[position] = card


def insert(deck, position, card):
    deck._cards.insert(position, card)


print("Before:", FrenchDeck2.__dict__)
FrenchDeck2.__abstractmethods__ = None  # 将子类中的__abstractmethods__方法置空，可以使用猴子补丁。
FrenchDeck2.__setitem__ = setitem
FrenchDeck2.insert = insert
print("After:", FrenchDeck2.__dict__)

try:
    deck3 = FrenchDeck2()
    shuffle(deck3)
    print("deck3 init success!")
except:
    traceback.print_exc()  # 抽象基类的子类无法通过猴子补丁的方式更新类的抽象方法，在于关键字__abstractmethods__
