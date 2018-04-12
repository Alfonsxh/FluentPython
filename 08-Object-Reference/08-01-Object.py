#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 08-01-Object.py
@time: 18-3-4 上午10:50
@version: v1.0 
"""


class test1:
    def __init__(self):
        print("hello test1 id is -> %s" % id(self))


x = test1()

# 标识、相等性、别名
job = {"name": "Job L Benjain", "born": "1932"}
job_copy = job

print("job is job_copy?", job is job_copy)
print("id(job), id(job_copy):".rjust(30), id(job), id(job_copy))
job_copy["blanance"] = 953
print("job:".rjust(30), job)

# == 比较的是值,is比较的是内存地址
tom = {'name': 'Job L Benjain', 'born': '1932', 'blanance': 953}

print("job == tom:".rjust(30), job == tom)
print("job is tom:".rjust(30), job is tom)

# 列表做浅复制
print("*" * 32 + "列表做浅复制" + "*" * 32)
l1 = [3, [4, 5], (6, 7, 8)]
l2 = list(l1)
print("id(l1) == id(l2):", id(l1) == id(l2))  # l1,l2的id不同
print("id(l1[1])==id(l2[1]):", id(l1[1]) == id(l2[1]))  # l1,l2内部的id相同

l3 = l1
print("id(l1) == id(l3):", id(l1) == id(l3))  # l1,l3所指为同一个盒子
print("id(l1[1])==id(l3[1]):", id(l1[1]) == id(l3[1]))
