#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 02-05-numpy-scipy.py
@time: 2017/12/27 21:01
@version: v1.0
"""
# 内存视图
str_a = b"abcdefg"
str_memv = memoryview(b"abcdefg")
print(str_memv.readonly)
# str_memv[2] = 't'  # 错误，str只读不能改变值

byte_array = bytearray("abcdef", "utf-8")
byte_array_memv = memoryview(byte_array)
print(byte_array_memv.readonly)
byte_array_memv[3] = 76
print(byte_array)

from array import array
array_a = array('h', [-1, -2, 0, 1, 2])
array_mmev = memoryview(array_a)
print(array_mmev.readonly)
array_oct = array_mmev.cast('B')
print(array_oct.tolist())
array_oct[5] = 4
print(array_a)

# 使用memoryview的时间差异对比
import time
for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print('bytes', n, time.time()-start)

for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)

# Numpy 和 Scipy
