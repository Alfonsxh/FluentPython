"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 19-01-Attribute.py
@time: 18-8-13 下午11:01
@version: v1.0 
"""
import os
import requests
import json

DATA_URL = "http://www.oreilly.com/pub/sc/osconfeed"
STORE_FILE = "data/osconfeed.json"


def Load():
    if not os.path.exists(STORE_FILE):
        os.makedirs(os.path.dirname(STORE_FILE), exist_ok=True)

        json_data = requests.get(DATA_URL).content

        with open(STORE_FILE, "wb") as f:
            f.write(json_data)

    with open(STORE_FILE, "rb") as f:
        return json.load(f)


if __name__ == "__main__":
    jsonData = Load()

    print(sorted(jsonData["Schedule"].keys()))

    for key, value in sorted(jsonData["Schedule"].items()):
        print("{:3} {}".format(len(value), key))

    print("\nThe last speaker is {}.".format(jsonData["Schedule"]["speakers"][-1]["name"]))
    print("The last speaker serial is {}.".format(jsonData["Schedule"]["speakers"][-1]["serial"]))

