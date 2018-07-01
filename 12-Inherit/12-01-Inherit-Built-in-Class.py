#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 12-01-Inherit-Built-in-Class.py
@time: 18-4-25 下午10:03
@version: v1.0 
"""

print("使用内置的dict类型子类化：")


# 不要子类化内置类型：list、dict等，他们都由c语言底层实现。
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)  # __init__没有使用__setitem__进行初始化
print(dd)
dd["two"] = 2  # []运算符会覆盖__setitem__方法
print(dd)
dd.update(three=3)  # update方法不会使用__setitem__
print(dd)

print("\n\n使用collections的UserDict类型子类化：")
# 使用collections模块中UserDict、UserList、UserString进行子类化
import collections


class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd2 = DoppelDict2(one=1)  # __init__使用__setitem__进行初始化
print(dd2)
dd2["two"] = 2  # []运算符会覆盖__setitem__方法
print(dd2)
dd2.update(three=3)  # update方法使用__setitem__
print(dd2)
