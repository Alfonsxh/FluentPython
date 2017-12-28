#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 01-01-porker.py
@time: 2017/12/5 21:42
@version: v1.0
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from collections import namedtuple

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

    def __setitem__(self, position, card):
        self._cards[position] = card

    def __delitem__(self, position):
        del self._cards[position]


if __name__ == "__main__":
    card = Card(7, "hearts")
    print(card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[5])

    from random import choice, shuffle

    print(choice(deck))   # 选择一个元素
    print(choice(deck))
    shuffle(deck)   # 打乱列表顺序
    print(deck[:10])
    shuffle(deck)
    print(deck[:10])
    pass
