"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 19-05-Shelve1.py
@time: 18-8-17 下午10:36
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

DB_NAME = "data/schedule1_db"
CONFERENCE = "conference.115"


class RecordClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def LoadDB(db):
    raw_data = Load()
    warnings.warn("loading " + DB_NAME)
    for collection, res_list in raw_data["Schedule"].items():
        record_type = collection[:-1]
        for record in res_list:
            key = "{}.{}".format(record_type, record["serial"])  # 以record_type.serial的形式记录key值
            record["serial"] = key
            db[key] = RecordClass(**record)  # 以record_type.serial为key将值存储在db中


if __name__ == "__main__":
    import shelve  # 将内存中的对象以字典的形式存储在文件中，key必须为字符串，value可为任意

    db = shelve.open(DB_NAME)
    if CONFERENCE not in db:
        LoadDB(db)

    speaker = db["speaker.3471"]
    print(type(speaker))  # 类型为Recoed类对象
    print((speaker.name, speaker.twitter))
    print(speaker.__dict__)
    db.close()
