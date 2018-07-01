"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 15-02-While.py
@time: 18-7-1 下午10:42
@version: v1.0 
"""

i = 0
while i <= 10:
    print("This {i} time execute!".format(i=i))
    i += 1
else:
    print("I'm else!")  # 执行玩循环体退出后执行
