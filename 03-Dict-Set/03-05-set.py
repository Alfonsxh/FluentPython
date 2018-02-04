#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 03-05-set.py
@time: 18-2-4 下午8:30
@version: v1.0 
"""
list_1 = ["he", "me", "he", "le"]
l_set = set(list_1)
print(l_set)
print(list(l_set))

list_2 = [1]
l_set = set(list_2)

from unicodedata import name

set_str = {chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), '')}
print(set_str)
pass

