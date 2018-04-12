#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 10-01-vector.py
@time: 18-4-12 下午9:58
@version: v1.0 
"""
from array import array
import math
import reprlib
import numbers
import operator
import functools


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
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))  # zip返回两个迭代， all返回只有所有比较都为True，才返回True

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


vector_a = Vector([3.0, 4.0])
print(vector_a)
print(repr(vector_a))

vector_b = Vector(range(1, 1000))
print(repr(vector_b))

print(repr(vector_b[2]))
print(repr(vector_b[2::2]))
print(repr(vector_b[2:-1:2]))
print(repr(vector_b[:10:2]))
# print(repr(vector_b[1, 2]))   # 抛出异常e 4

print(vector_b.x)
vector_b.X = 1000008
print(repr(vector_b.X))
print(hash(vector_b))
print(vector_b == vector_b)
print(vector_b == vector_a)
