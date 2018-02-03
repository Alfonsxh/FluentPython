#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 02-03-slice.py
@time: 2017/12/24 22:40
@version: v1.0
"""
# 切片
s = "bicycle"
slice_a = s[::3]
slice_b = s[::-2]
slice_c = s[::-1]
print(slice_a)
print(slice_b)
print(slice_c)

invoice = """
1909 Pimoroni PiBrella         $17.50 3 $52.50
1489 6mm Tactile Switch x20    $4.95  2 $9.90
1510 Panavise Jr. - PV-201     $28.00 1 $28.00
1601 PiTFT Mini Kit 320x240    $34.95 1 $34.95
"""
for item in invoice.split("\n"):
    SKU = slice(0, 5)
    DESCRIPTION = slice(5, 31)
    PRICE = slice(31, 37)
    print(item[SKU], item[DESCRIPTION], item[PRICE])

# 多维切片
import numpy

# 给切片赋值
l = list(range(10))
print(l)
l[2:5] = [98, 99]
print(l)
del l[8:9]
print(l)
l[3::2] = [2222, 3333, 4444]
print(l)

# 序列的 + 与 * 操作
board = [['_'] * 3 for i in range(3)]
print(board)
board[2][2] = 'X'
print(board)

print("Diff with down.↓")

board = [['_'] * 3] * 3
print(board)
board[2][2] = 'X'
print(board)

# 增量赋值
l = [range(3)]
print(id(l))
l *= 3
print(id(l))
t = (1, 2, 3)
print(id(t))
t *= 3
print(id(t))

# 关于+= 有趣的例子
t = (1, 2, [50, 60])
try:
    t[2] += [20]
except:
    print("Except happend!")
    pass
print(t)

# list.sort 与内置sorted函数
fruits = ["grape", "raspberry",  "apple", "banana"]
print(sorted(fruits))
print(sorted(fruits, key = len))
print(sorted(fruits, reverse = True))
print(sorted(fruits, key = len, reverse = True))
print(fruits)        # 不改变列表的原始值
fruits.sort()
print(fruits)        # 改变列表的原始值