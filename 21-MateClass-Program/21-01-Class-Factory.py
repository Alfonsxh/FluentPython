"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 21-01-Class-Factory.py
@time: 18-8-26 下午11:51
@version: v1.0 
"""


# 使用RecordFactory函数创建的类无法序列化
def RecordFactory(cls_name: str, field_names: str):
    try:
        field_names = field_names.replace(',', " ").split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for key, value in attrs.items():
            setattr(self, key, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ", ".join("{} = {!r}".format(*i) for i in zip(self.__slots__, self))
        return "{}({})".format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    return type(cls_name, (object,), cls_attrs)


Dog = RecordFactory("DogClass", "name weight ower")

rex = Dog("rex", 30, "Alice")
print(rex)
for value in rex:
    print(value)
