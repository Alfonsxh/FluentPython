"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 19-06-Shelve2.py
@time: 18-8-18 上午10:54
@version: v1.0 
"""
import os
import requests
import json

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


import warnings

DB_NAME = "data/schedule2_db"
CONFERENCE = "conference.115"


class RecordClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        pass

    def __eq__(self, other):
        if isinstance(other, RecordClass):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class DBRecord(RecordClass):
    __db = None

    @staticmethod
    def SetDB(db):
        DBRecord.__db = db

    @staticmethod
    def GetDB():
        return DBRecord.__db

    @classmethod
    def Fetch(cls, key):
        """
        根据key值选取目标数据
        :param key: 要选取的属性名
        :return: 属性所属的值
        """
        db = cls.GetDB()

        try:
            # for i in db:
            #     print(i)
            return db[key]
        except TypeError:
            if db is None:
                raise RuntimeError("Database not set; call '{}.SetDB(db)'".format(cls.__name__))
            else:
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return "<{} serial={!r}>".format(cls_name, self.serial)
        else:
            return super.__repr__()


class Event(DBRecord):

    @property  # 将Venue作为Event类的属性
    def Venue(self):  # 会场信息，对应json中的venues中的元素
        key = "venue.{}".format(self.venue_serial)
        return self.__class__.Fetch(key)

    @property  # 类似于Venue属性
    def Speaker(self):  # 演讲者信息，对应json中的speakers中的元素
        if not hasattr(self, "_speaker_objs"):
            spkr_serials = self.__dict__["speakers"]
            fetch = self.__class__.Fetch  # 防止数据中含有名为‘Fetch’的键。此处确保fetch为父类的方法
            self._speaker_objs = [fetch("speaker.{}".format(key)) for key in spkr_serials]

        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, "name"):
            return "<{} {!r}>".format(self.__class__.__name__, self.name)
        else:
            return super().__repr__()


import inspect


def LoadDB(db):
    """
    使用先前的数据做初始化
    :param db: 之前的db文件
    :return:
    """
    raw_data = Load()
    warnings.warn("loading " + DB_NAME)
    for collection, res_list in raw_data["Schedule"].items():
        record_type = collection[:-1]

        cls_name = record_type.capitalize()  # 将首字母大写，匹配类名
        cls = globals().get(cls_name, DBRecord)  # 从全局变量中获取类，默认使用RecordClass类代替
        if inspect.isclass(cls) and issubclass(cls, DBRecord):
            factory = cls
        else:
            factory = DBRecord

        for record in res_list:  # 记录events、speakers、venues中各元素的信息
            key = "{}.{}".format(record_type, record["serial"])  # 以record_type.serial的形式记录key值
            record["serial"] = key
            db[key] = factory(**record)  # 以record_type.serial为key将值存储在db中，如event.serial、speaker.serial、venue.serial


if __name__ == "__main__":
    import shelve

    db = shelve.open(DB_NAME)
    if CONFERENCE not in db:
        LoadDB(db)

    DBRecord.SetDB(db)
    event = DBRecord.Fetch("event.33950")
    print(event)
    venue = event.Venue  # 调用 Event类的Venue方法
    print(venue)
    print(event.Venue.name)     # 打印活动的主题

    print("\n\n")

    for spkr in event.Speaker:          # 打印与活动相关的演讲者的信息
        print("{speaker.serial}: {speaker.name}".format(speaker=spkr))

    db.close()
