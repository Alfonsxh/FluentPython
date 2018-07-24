"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 16-03-YieldFrom.py
@time: 18-7-24 下午9:37
@version: v1.0 
"""


# 功能一：省去for循环的调用
# yield from 可将可迭代对象转化为生成器

def gen0():
    for char in "ABC":
        yield char

    for num in range(7):
        yield num


genList = list(gen0())
print(genList)


def gen():
    yield from "ABC"
    yield from range(7)


genList = list(gen())
print(genList)
