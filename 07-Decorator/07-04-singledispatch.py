#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 07-04-singledispatch.py
@time: 18-2-28 下午8:40
@version: v1.0 
"""
from functools import singledispatch
import html


# 单分派泛函数，实现重载
@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return "<pre>%s</pre>" % content


@htmlize.register(str)
def func1(text):
    content = html.escape(text).replace("\n", "<br>\n")
    return "<p>%s</p>" % content


@htmlize.register(int)
def func1(num):
    return "<pre>{0} (0x{0:x})</pre>".format(num)


@htmlize.register(list)
def func1(lst):
    content = "</li>\n<li>".join(htmlize(enum) for enum in lst)
    return "<ul>\n<li>%s</li>\n</ul>" % content


print("htmlize({1, 2, 3}:".rjust(30), htmlize({1, 2, 3}))
print("""htmlize("helllo"):""".rjust(30), htmlize("helllo"))
print(" htmlize(['jels', 54, {1, 2, 3}]):\n", htmlize(['jels', 54, {1, 2, 3}]))

print(":".rjust(30), )
print("*" * 32 + "" + "*" * 32)
