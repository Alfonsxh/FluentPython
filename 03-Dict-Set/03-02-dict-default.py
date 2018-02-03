#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 03-02-dict-default.py
@time: 2018/1/30 20:10
@version: v1.0 
"""

"""统计文本中单词位置的三种方式"""

import re
import collections

re = re.compile("\w+")  # 匹配所有单词


def DefaultFunc1():
    """一般方式"""
    index = {}
    with open("words.txt", encoding = "utf-8") as f:
        for line_no, line in enumerate(f, 1):
            for match in re.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # 下面代码不好
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences
    for word in sorted(index, key = str.upper):
        print(word, index[word])


def DefaultFunc2():
    """使用setdefault方法"""
    index = {}
    with open("words.txt", encoding = "utf-8") as f:
        for line_no, line in enumerate(f, 1):
            for match in re.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                index.setdefault(word, []).append(location)

    for word in sorted(index, key = str.upper):
        print(word, index[word])


def DefaultFunc3():
    """使用defaultdict"""
    index = collections.defaultdict(list)
    with open("words.txt", encoding = "utf-8") as f:
        for line_no, line in enumerate(f, 1):
            for match in re.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                index[word].append(location)

    for word in sorted(index, key = str.upper):
        print(word, index[word])


DefaultFunc1()
DefaultFunc2()
DefaultFunc3()
