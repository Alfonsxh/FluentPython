"""
@author: Alfons
@contact: alfons_xh@163.com
@file: evalsupport.py
@time: 18-9-3 下午10:47
@version: v1.0 
"""
print("<[100]> Evalsupport moudle start")


def ClsDecorator(cls):
    print("<[200]> Class Decorator body")

    def Method(self):
        print("<[300]> Class method changes")

    cls.MethodY = Method
    return cls


class MetaAleph(type):
    print("<[400]> MetaAleph body")

    def __init__(cls, name, bases, dic):
        print("<[500]> MetaAleph.__init__")

        def MethodZ(self):
            print("<[600]> MetaAleph.MethodZ")

        cls.MethodZ = MethodZ


print("<[700]> Evalsupport moudle end")
