"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 19-02-Attribute-Getattr1.py
@time: 18-8-15 下午8:57
@version: v1.0 
"""
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
    def __init__(self, mapping):
        self.__data = dict()
        for key, value in mapping.items():  # 防止含有关键字的键值对
            if keyword.iskeyword(key):  # 判断是否是python关键字
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):  # 查看目标对象是否含有指定的属性
            return getattr(self.__data, name)  # 获取目标的对象指定的属性
        else:
            res = FrozenJSON.build(self.__data[name])
            return res

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)  # 如果是字典，则返回类似的类
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]  # 如果是列表类型，则返回cls类型的列表
        else:
            return obj  # 如果是其他类型，则返回原始数据，如string类型等


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
