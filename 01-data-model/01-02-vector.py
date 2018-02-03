#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 01-02-vector.py
@time: 2017/12/11 22:13
@version: v1.0
"""
from math import hypot


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector( %r, %r )" % (self.x, self.y)

    def __bool__(self):
        return self.x or self.y

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


if __name__ == "__main__":
    vec_a = Vector(1, 3)
    vec_b = Vector(5, 1)
    print(vec_a, vec_b)
    vec_c = vec_a + vec_b
    print(vec_c)
    vec_d = vec_a * vec_b
    print(vec_d)
    pass