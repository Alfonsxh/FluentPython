"""
@author: Alfons
@contact: alfons_xh@163.com
@file: test.py
@time: 18-8-28 下午9:28
@version: v1.0 
"""


class Circle1(object):
    def __init__(self, radius):
        self.radius = radius  # 属性

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2


class Circle2(object):
    def __init__(self, radius):
        self.radius = radius  # 属性

    def getdiameter(self):
        return self.radius * 2

    def setdiameter(self, new_diameter):
        self.radius = new_diameter / 2

    diameter = property(getdiameter, setdiameter)  # 特性


circle1 = Circle1(2)

print(circle1.radius)
print(circle1.diameter)

circle2 = Circle2(2)

print(circle2.radius)
print(circle2.diameter)


class Info(object):
    # __slots__ = ("name", "__data", "allowattr")

    def __init__(self, mapping):
        self.name = "test_info"
        self.__data = dict(mapping)

    def __getattr__(self, item):
        print("Find attribute {} through __getattr__.".format(item))
        if item in self.__data.keys():
            return self.__data[item]
        else:
            return "ValueError"


info = Info(dict(radius=1, diameter=2))
print(info.name)
print(info.radius)
print(info.area)
print(hasattr(info, "__data"))
setattr(info, "name", "name_change")
print(info.name)
print(info.__dict__)

info.allowattr = 4
print(info.allowattr)
info.notallowattr = 5

print(dir(info))
print(vars(info))