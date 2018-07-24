"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 16-02-Averager.py
@time: 18-7-23 下午11:00
@version: v1.0 
"""

from inspect import getgeneratorstate


# 使用协程求平均值
def Averager0():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


avg0 = Averager0()
print("getgeneratorstate(avg0) -> ", getgeneratorstate(avg0))
print("next(coroAvg) -> ", next(avg0))
print("avg0.send(10) -> ", avg0.send(10))
print("avg0.send(11) -> ", avg0.send(11))
print("avg0.send(12) -> ", avg0.send(12))
print("avg0.send(13) -> ", avg0.send(13))
print("avg0.send(14) -> ", avg0.send(14))
print("\n\n")


# 预激协程的装饰器
def coroutine(func):
    from functools import wraps

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def Averager1():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


avg1 = Averager1()
print("getgeneratorstate(avg1) -> ", getgeneratorstate(avg1))
print("avg1.send(10) -> ", avg1.send(10))
print("avg1.send(11) -> ", avg1.send(11))
print("avg1.send(12) -> ", avg1.send(12))
print("avg1.send(13) -> ", avg1.send(13))
print("avg1.send(14) -> ", avg1.send(14))
print("avg1.close() -> ", avg1.close())
print("getgeneratorstate(avg1) -> ", getgeneratorstate(avg1))
print("\n\n")


from collections import namedtuple

Result = namedtuple("Result", "count,average")


def Averager2():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


avg2 = Averager2()
next(avg2)
print("getgeneratorstate(avg2) -> ", getgeneratorstate(avg2))
print("avg2.send(10) -> ", avg2.send(10))
print("avg2.send(11) -> ", avg2.send(11))

try:
    print("avg2.send(None) -> ", avg2.send(None))
except StopIteration as exc:
    print("Result -> ", exc)
