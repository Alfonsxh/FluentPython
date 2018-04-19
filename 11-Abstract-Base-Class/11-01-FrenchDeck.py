#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 11-01-FrenchDeck.py
@time: 18-4-18 下午9:35
@version: v1.0 
"""
from collections import namedtuple
from random import shuffle

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
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


deck = FrenchDeck()
try:
    shuffle(deck)
except:
    print("shuffle error!")


# 打猴子补丁
def set_card(deckSelf, position, card):
    deckSelf._cards[position] = card        # 打补丁时，必须要知道deck对象中含有_cards属性


FrenchDeck.__setitem__ = set_card
shuffle(deck)
print("shuffle success!")
