#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 02-01-list-comps.py
@time: 2017/12/24 21:26
@version: v1.0 
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 列表推导
symbols = "@#$%^&*()_+{}[]:';>?<?>'"
codes = [ord(symbols) for symbols in symbols]
print codes
print symbols  # python2 打印 ‘    python3 打印原字符串

# filter、map实现列表推导
symbols = "@#$%^&*()_+{}[]:';>?<?>'"
first_ascii = [ord(c) for c in symbols if ord(c) > 60]
print first_ascii
second_ascii = list(filter(lambda c: c > 60, map(ord, symbols)))
print second_ascii

# 使用列表推导计算笛卡儿积
ranks = [str(n) for n in range(2, 11)] + list("JQKA")
suits = "spades diamonds clubs hearts".split()  # 4种花色
cards = [(rank, suit) for rank in ranks
                      for suit in suits]
print cards

# 生成器表达式
symbols = "@#$%^&*()_+{}[]:';>?<?>'"
symbol_tuple = tuple(ord(c) for c in symbols)
print symbol_tuple

import array
symbol_array = array.array('I', (ord(c) for c in symbols))
print symbol_array

# 列表推导会产生一个临时列表，生成器逐个产生元素

pass