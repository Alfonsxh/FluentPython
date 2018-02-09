#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 04-01-Encode-Decode.py
@time: 18-2-9 下午8:38
@version: v1.0 
"""
# 简单的编码和解码
# encode为编码过程，将码位转换为计算机识别的字节序列
# decode为解码过程，将计算机识别的字节序列转换为人类识别的码位
print("*" * 32 + "简单的编码和解码" + "*" * 32)
cafe_s = 'café'
print("cafe_str:".rjust(30), cafe_s)
print("cafe_str's length:".rjust(30), len(cafe_s))
cafe_b = cafe_s.encode("utf-8")
print("cafe_bytes:".rjust(30), cafe_b)  # 编码成bytes对象后，字符串长度改变
print("cafe_bytes's length:".rjust(30), len(cafe_b))

# bytes对象
print("*" * 32 + "bytes对象" + "*" * 32)
cafe_bytes = bytes(cafe_s, encoding="utf-8")
print("cafe_bytes[0]:".rjust(30), cafe_bytes[0])
print("cafe_bytes[:1]:".rjust(30), cafe_bytes[:1])  # bytes对象的切片有字面量变量 ----> b

# bytearray对象
print("*" * 32 + "bytearray对象" + "*" * 32)
cafe_arr = bytearray(cafe_s, encoding="utf-8")
print("cafe_arr:".rjust(30), cafe_arr)
print("cafe_arr[0]:".rjust(30), cafe_arr[0])
print("cafe_arr[:1]:".rjust(30), cafe_arr[:1])  # bytearray对象的切片还是bytearry对象

# 结构体和memooryview
print("*" * 32 + "结构体和memooryview" + "*" * 32)
import struct

fmt = "<3s3sHH"
with open("1.gif", "rb") as f:
    img = memoryview(f.read())

header = img[0:10]
print("bytes(header):".rjust(30), bytes(header))
print("struct.unpack(fmt, header):".rjust(30), struct.unpack(fmt, header))
del header
del img
