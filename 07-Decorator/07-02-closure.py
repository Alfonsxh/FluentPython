#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 07-02-closure.py
@time: 18-2-26 下午9:55
@version: v1.0 
"""
# python 闭包以及nonlocal关键字
print("*" * 32 + "python 闭包以及nonlocal关键字" + "*" * 32)


# 使用类实现
class Average():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)


avg1 = Average()
print("avg1(10):".rjust(30), avg1(10))
print("avg1(10.5):".rjust(30), avg1(10.5))
print("avg1(11):".rjust(30), avg1(11))
print("\n")


# 使用函数实现
def MakeAverage():
    series = []

    def Average(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return Average


avg2 = MakeAverage()
print("avg2(10):".rjust(30), avg2(10))
print("avg2(10.5):".rjust(30), avg2(10.5))
print("avg2(11):".rjust(30), avg2(11))
print("\n")


def MakeAverage2():
    total = 0
    count = 0

    def Average2(new_value):
        nonlocal total, count  # nonlocal关键字将变量标记为自有变量
        total += new_value
        count += 1
        return total / count

    return Average2


avg3 = MakeAverage2()
print("avg3(10):".rjust(30), avg3(10))
print("avg3(10.5):".rjust(30), avg3(10.5))
print("avg3(11):".rjust(30), avg3(11))

print(":".rjust(30), )
print("*" * 32 + "" + "*" * 32)
