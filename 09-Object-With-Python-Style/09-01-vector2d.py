#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 09-01-vector2d.py
@time: 18-4-11 下午10:00
@version: v1.0 
"""
from array import array
import math


class Vector2d:
    typecode = 'd'
    __slots__ = ("__x", "__y")      # 使用tuple存放数据，而非__dict__。实例数量百万级时使用

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):            # 设置只读属性，可散列对象值不可变
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):  # 使类变为可散列对象
        return tuple(self) == tuple(other)

    def __hash__(self):         # 使类变为可散列对象
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):             # 从bytes中恢复数据
        typecode = octets[0]
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, format_spec = ""):     # format方法
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), math.atan2(self.y, self.x))
            outfm = "<{}, {}>"
        else:
            coords = self
            outfm = "({}, {})"
        components = (format(f, format_spec) for f in coords)
        return outfm.format(*components)


vector_2d = Vector2d(1, 2)
print(vector_2d)
x, y = vector_2d
print(x, y)
print(format(vector_2d, ".3f"))


# print(":".rjust(30),)
# print("*" * 32 + "" + "*" * 32)
