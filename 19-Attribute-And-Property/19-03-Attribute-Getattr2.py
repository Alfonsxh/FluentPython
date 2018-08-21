"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 19-03-Attribute-Getattr2.py
@time: 18-8-15 下午10:14
@version: v1.0 
"""

# __new__方法介绍：https://www.cnblogs.com/ifantastic/p/3175735.html

import os
import requests
import json
from collections import abc
import keyword

DATA_URL = "http://www.oreilly.com/pub/sc/osconfeed"
STORE_FILE = "data/osconfeed.json"


def Load():
    """
    加载目标json数据
    :return: 数据的dict格式
    """
    if not os.path.exists(STORE_FILE):
        os.makedirs(os.path.dirname(STORE_FILE), exist_ok=True)

        json_data = requests.get(DATA_URL).content

        with open(STORE_FILE, "wb") as f:
            f.write(json_data)

    with open(STORE_FILE, "rb") as f:
        return json.load(f)


class FrozenJSON:
    def __init__(self, mapping):    # __init__初始化属性
        self.__data = dict()
        for key, value in mapping.items():  # 防止含有关键字的键值对
            if keyword.iskeyword(key):  # 判断是否是python关键字
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):  # 查看目标对象是否含有指定的属性
            return getattr(self.__data, name)  # 获取目标的对象指定的属性
        else:
            res = FrozenJSON(self.__data[name])
            return res

    def __new__(cls, arg):      # 使用__new__替代build函数,__new__产生实例
        if isinstance(arg, abc.Mapping):
            # return cls(obj)
            return super().__new__(cls)         # 返回FrozenJSON的实例
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg  # 如果是其他类型，则返回原始数据，如string类型等


if __name__ == "__main__":
    jsonData = FrozenJSON(Load())

    print(sorted(jsonData.Schedule.keys()))

    for key, value in sorted(jsonData.Schedule.items()):
        print("{:3} {}".format(len(value), key))

    print("\nThe last speaker is {}.".format(jsonData.Schedule.speakers[-1].name))
    print("The last speaker serial is {}.".format(jsonData.Schedule.speakers[-1].serial))

    jsonData = FrozenJSON({"class": "hello", "print": "world", "2e": "china"})
    print("\njsonData.class_ -> ", jsonData.class_)
    print("jsonData.print -> ", jsonData.print)
    # print("jsonData.2e -> ", jsonData.2e)         # 非有效字符
