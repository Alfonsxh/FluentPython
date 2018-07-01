#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 13-01-Vector.py
@time: 18-5-15 下午10:05
@version: v1.0 
"""

from array import array
import math
import reprlib
import numbers
import operator
import functools
import itertools
import traceback


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self.__components = array(self.typecode, components)

    def __len__(self):
        return len(self.__components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self.__components[index])
        elif isinstance(index, numbers.Integral):
            return self.__components[index]
        else:
            raise TypeError("{cls.__name__} indices must be integers".format(cls=cls))

    def __iter__(self):
        return iter(self.__components)

    def __repr__(self):
        component_str = reprlib.repr(self.__components)
        component_str = component_str[component_str.find('['):-1]  # 也可使用list转换，但代价太大
        return "Vector({})".format(component_str)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self.__components)

    def __eq__(self, other):  # 比较方案改进，适用于超长的数组
        # return tuple(self) == tuple(other)
        return len(self) == len(other) and all(
            a == b for a, b in zip(self, other))  # zip返回两个迭代， all返回只有所有比较都为True，才返回True

    def __hash__(self):
        hashes = (hash(x) for x in self)  # 使用了生成器，内部有yield产生参数
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    shortcut_names = "xyzt"

    def __getattr__(self, name):  # vector 类能够使用 vector.x vector.y 来获取对应位置的值
        cls = type(self)  # type 返回类中的参数
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self.__components):
                return self.__components[pos]
        raise AttributeError("{.__name__} object has no attribute {}".format(cls, name))

    def __setattr__(self, name, value):  # 设置 vector 为只读属性
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "can't set 'a' to 'z' in {cls_name!r}"
            else:
                error = ""

            if error:
                raise AttributeError(error.format(attr_name=name, cls_name=cls.__name__))
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec=""):
        if format_spec.endswith('h'):
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outfm = "<{}>"
        else:
            coords = self
            outfm = "({})"
        components = (format(f, format_spec) for f in coords)
        return outfm.format(",".join(components))


vector_a = Vector([3.0, 4.0])
print("vector_a:", vector_a)

vector_b = Vector([8, 9, 10])
print("vector_b:", vector_b)

print("\n重载+运算符前：")

try:
    vector_c = vector_a + vector_b
except:
    traceback.print_exc()

print("\n重载+运算符后：")


def add(self, other):
    try:
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)
    except TypeError:
        return NotImplemented


def addr(self, other):
    return self + other


Vector.__add__ = add
Vector.__radd__ = addr

print("vector_a + vector_b = ", vector_a + vector_b)
print("vector_a + [1,2,3,4,5] = ", vector_a + [1, 2, 3, 4, 5])
print("[1,2,3,4,5] + vector_a  = ", [1, 2, 3, 4, 5] + vector_a)
# print("'ABC' + vector_a  = ", 'ABC' + vector_a)

print("\n重载*运算符后：")

import numbers


def mul(self, scalar):
    if isinstance(scalar, numbers.Real):
        return Vector(a * scalar for a in self)
    else:
        return NotImplemented


def rmul(self, scalar):
    return self * scalar


Vector.__mul__ = mul
Vector.__rmul__ = rmul

print("vector_a * 7 = ", vector_a * 7)
print("7 * vector_a = ", 7 * vector_a)

from fractions import Fraction
i = Fraction(1, 3)
j = 1/3
print("vector_a * i = ", vector_a * i)
print("vector_a * j = ", vector_a * j)
pass
