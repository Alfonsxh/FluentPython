#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 03-01-dict.py
@time: 2017/12/28 22:34

@version: v1.0 
"""
# 字典
from collections import abc

my_dict = {}
print("isinstance(my_dict, abc.Mapping):", isinstance(my_dict, abc.Mapping))
print("isinstance(my_dict, dict):", isinstance(my_dict, dict))
print("isinstance(my_dict, list):", isinstance(my_dict, list))

# 字典初始化
a = dict(one = 1, two = 2, three = 3)
b = {"one": 1, "two": 2, "three": 3}
c = dict(zip(["one", "two", "three"], [1, 2, 3]))
d = dict([("one", 1), ("two", 2), ("three", 3)])
e = dict({"one": 1, "two": 2, "three": 3})

print(a, b, c, d, e)
print("a == b == c == d == e:", a == b == c == d == e)

# 字典推导
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
print("country_code:", country_code)
print("country_code:", {code: country.upper() for country, code in country_code.items() if code < 86})
