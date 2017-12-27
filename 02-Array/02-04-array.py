#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 02-04-array.py
@time: 2017/12/27 20:35
@version: v1.0 
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 数组
from array import array
from random import random

# float_count = 10**7
# float_array = array('d', (random() for i in range(float_count)))
# print float_array[-1]
# print len(float_array)
# with open("floats.bin", "wb") as f:
#     float_array.tofile(f)
#
# float_array_2 = array('d')
# with open("floats.bin", "rb") as f:
#     float_array_2.fromfile(f, float_count)
# print float_array_2[-1]
# print len(float_array_2)
# pass