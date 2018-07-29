"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 17-03-Flags-Futures-ThreadPool2.py
@time: 18-7-29 下午2:28
@version: v1.0 
"""

import os
import time
import requests
import concurrent.futures as futures

BASE_URL = "http://flupy.org/data/flags/"
DEST_DIR = "flags_futures_thread2/"

FLAGS_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()

MAX_WORLERS = 20


def SaveFlag(img, filename):
    savePath = os.path.join(DEST_DIR, filename.lower())
    with open(savePath, "wb") as f:
        f.write(img)


def Show(flag):
    print(flag, end=" ")


def GetFlag(flag):
    downloadUrl = "{base}/{flag}/{flag}.gif".format(base=BASE_URL, flag=flag.lower())
    ret = requests.get(downloadUrl)
    content = ret.content
    return content


def DownloadOne(flag):
    image = GetFlag(flag)
    Show(flag)
    SaveFlag(image, flag.lower() + ".gif")
    return flag


# 使用submit和as_completed完成相同的步骤
def DownloadFlags(flagList: list):
    workers = min(MAX_WORLERS, len(flagList))
    with futures.ThreadPoolExecutor(workers) as executor:
        # res = exector.map(DownloadOne, sorted(flagList))  # 使用线程池来下载

        toDo = list()
        for flag in sorted(flagList):
            future = executor.submit(DownloadOne, flag)  # 传入处理函数和参数，为其安排future时间处理
            toDo.append(future)

        res = list()
        for future in futures.as_completed(toDo):  # 输入参数为future列表，返回值为迭代器
            result = future.result()  # concurrent.futures的result()方法含有timeout参数
            res.append(result)
    return len(list(res))


def main(flagsList):
    os.makedirs(DEST_DIR, exist_ok=True)

    startTime = time.time()
    counts = DownloadFlags(flagsList)
    endTime = time.time()

    print("\nDownload {} flags in {}'s.".format(counts, endTime - startTime))


if __name__ == "__main__":
    main(FLAGS_CC)
