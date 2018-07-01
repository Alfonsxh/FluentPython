#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 12-02-Multiple-Inheritance.py
@time: 18-4-25 下午10:14
@version: v1.0 
"""


class A:
    def ping(self):
        print('ping', self)


class B(A):
    def pong(self):
        print('pong', self)


class C(A):
    def pong(self):
        print('PONG_BIG', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()

        super().ping()
        self.pong()
        super().pong()
        C.pong(self)  # 超类中的方法可以直接调用，要将实例作为显性参数传入


print("D.__mro__:", D.__mro__)  # 继承顺序为B、C、A
d = D()
print("\nd.pingpong():")
d.pingpong()  # 先调用D中重写的ping，再调用A的ping

import tkinter

print("\ntkinter.Toplevel.__mro__:", tkinter.Toplevel.__mro__)
print("\ntkinter.Widget.__mro__:", tkinter.Widget.__mro__)
print("\ntkinter.Button.__mro__:", tkinter.Button.__mro__)
print("\ntkinter.Entry.__mro__:", tkinter.Entry.__mro__)
