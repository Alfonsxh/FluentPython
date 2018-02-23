#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 05-03-function-other.py
@time: 18-2-10 下午8:12
@version: v1.0 
"""
# 提取函数的属性
print("*" * 32 + "提取函数的属性" + "*" * 32)


def factorial(n, l=10):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print("factorial.__defaults:".rjust(30), factorial.__defaults__)

from inspect import signature

sig = signature(factorial)
print("str(sig):".rjust(30), str(sig))
print("sig.parameters.items():".rjust(30), sig.parameters.items())

