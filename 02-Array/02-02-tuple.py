#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 02-02-tuple.py
@time: 2017/12/24 22:17
@version: v1.0 
"""
# 元组
# 把元组用作记录
lax_coordinate = (21.321321, 32.12321321)  # 记录经纬度

# 元组拆包
beijing_info = ("Beijing", 2017, 2000, 0.32, 9230)
city, year, pop, chg, area = beijing_info
print(city, year, pop, chg, area)

# 无中间变量交换俩数的值
a = 43
b = 45
a, b = b, a
print("(a, b) = (%d, %d)" % (a, b))

# 使用* 处理元素(python3 特有)
# first, second, *rest = range(5)
# print  first, second, rest
# >>> 0, 1, [2, 3, 4]

# 嵌套元组拆包
city, year, pop, chg, area, (lng, lat) = ("Beijing", 2017, 2000, 0.32, 9230, (21.321321, 32.12321321))
print(city, year, pop, chg, area, (lng, lat))

# 具名元组
from collections import namedtuple
City = namedtuple("city", "name,country,population,coordinates")
beijing = City("Beijing", "China", "2300", (23.321312, 98.32323))
print(beijing)
print(beijing.population)
print(beijing.coordinates)

# 具名元组的其他属性和方法
print(City._fields)
print(beijing._asdict())