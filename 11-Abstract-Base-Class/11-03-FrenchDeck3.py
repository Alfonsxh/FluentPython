#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 11-03-FrenchDeck.py
@time: 18-4-18 下午9:35
@version: v1.0 
"""
from collections import namedtuple, MutableSequence
import traceback
from random import shuffle

Card = namedtuple("Card", ["rank", "suit"])


# FrenchDeck2，collections.MutableSequence的子类
class FrenchDeck3(MutableSequence):
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

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, card):
        self._cards.insert(position, card)

    def __setitem__(self, position, card):
        self._cards[position] = card


try:
    deck2 = FrenchDeck3()
    shuffle(deck2)
    print("deck2 init success!")        # 补上__setitem__、insert方法后，无异常
except:
    traceback.print_exc()