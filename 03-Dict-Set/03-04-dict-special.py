#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 03-04-dict-special.py
@time: 18-2-4 下午4:37
@version: v1.0 
"""

# 顺序字典,添加顺序保持
from collections import OrderedDict

order_dict = OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
order_dict["pi"] = "1"
print("order_dict:", order_dict.items())

normal_dict = dict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
normal_dict["pi"] = "1"
print("normal_dict:", normal_dict.items())

# 特殊方法
order_dict.popitem(last=False)  # 第一个元素出栈
print("order_dict:", order_dict.items())
order_dict.move_to_end("pear", last=False)  # pear至第一个
print("order_dict:", order_dict.items())

# ChainMap多个dict的集合
from collections import ChainMap

d1 = {1: 2, 3: 4, 5: 6}
d2 = {1: 1, 6: 7}

chain_map = ChainMap(d1, d2)
print(chain_map.get(1))

chain_map = ChainMap(d2, d1)
print(chain_map.get(1))

scm = chain_map.new_child({8: 9})
print(scm)
pcm = chain_map.parents
print(pcm)

# Counter dict中的元素计数
from collections import Counter

ct = Counter(order_dict)
print(ct)

ct = Counter("helksfiukkanikuioenlfasjlkj")
print(ct)
ct.update("12314412348217389712")
print(ct)

print(ct.most_common(5))  # 打印频率最高的前五个

# UserDict 将数据放在self.data 里面
from collections import UserDict


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


test_dict = StrKeyDict({"2": "two", "1": "one"})
print('test_dict["2"]:', test_dict["2"])
print('test_dict[1]:', test_dict[1])
try:
    print('test_dict[4]:', test_dict[4])  # 此处没有key为4的元素，报异常
except KeyError as ex:
    print("KeyError:", ex)

print('test_dict.get(1):', test_dict.get(1))
print('test_dict.get("2"):', test_dict.get('2'))
print('test_dict.get(4):', test_dict.get(4))  # 此处调用的为get()

print('2 in test_dict:', 2 in test_dict)
print('4 in test_dict:', 4 in test_dict)

# 不可变映射类型
from types import MappingProxyType
import traceback

d = {1: "a"}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
try:
    d_proxy[2] = "b"  # 赋值时出现异常，MappingProxyType类型没有定义__setitem__
except:
    traceback.print_exc()

pass
