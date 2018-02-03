#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 03-03-dict-missing.py
@time: 2018/1/30 20:53
@version: v1.0 
"""

"""
在 __getitem__ 碰到找不到的键的时候，Python 就会自动调用__missing__，
而不是抛出一个 KeyError 异常。
__missing__ 方法只会被 __getitem__ 调用（比如在表达式 d[k] 中）。
提供 __missing__ 方法对 get 或者__contains__（in 运算符会用到这个方法）
这些方法的使用没有影响
"""


class StrKeyDict(dict):
    def __missing__(self, key):
        """__missing__ 方法只会被 __getitem__ 调用，调用方式为 dict_a[key]"""
        if isinstance(key, str):
            raise KeyError(key)         # 此处已将key由 int ---> str
        return self[str(key)]           # 第一次进来，上面的判断失效，先调用此处

    def get(self, key, default = None):
        """__missing__ 不会被 get 调用"""
        try:
            return self[key]
        except KeyError:
            return "This is None"

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


test_dict = StrKeyDict({"2": "two", "1": "one"})
print('test_dict["2"]:', test_dict["2"])
print('test_dict[1]:', test_dict[1])
try:
    print('test_dict[4]:', test_dict[4])  # 此处没有key为4的元素，报异常
except KeyError as ex:
    print("KeyError:", ex)

print('test_dict.get(1):', test_dict.get(1))
print('test_dict.get("2"):', test_dict.get('2'))
print('test_dict.get(4):', test_dict.get(4))    # 此处调用的为get()

print('2 in test_dict:', 2 in test_dict)
print('4 in test_dict:', 4 in test_dict)

