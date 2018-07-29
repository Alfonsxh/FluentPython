"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 17-04-Flags-Futures-ProcessPool.py
@time: 18-7-29 下午2:28
@version: v1.0 
"""

import os
import time
import requests
import concurrent.futures as futures

BASE_URL = "http://flupy.org/data/flags/"
DEST_DIR = "flags_futures_process/"

FLAGS_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()


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


def DownloadFlags(flagList: list):
    with futures.ProcessPoolExecutor(os.cpu_count()) as exector:
        res = exector.map(DownloadOne, sorted(flagList))  # 使用线程池来下载
    return len(list(res))


def main(flagsList):
    os.makedirs(DEST_DIR, exist_ok=True)

    startTime = time.time()
    counts = DownloadFlags(flagsList)
    endTime = time.time()

    print("\nDownload {} flags in {}'s.".format(counts, endTime - startTime))


if __name__ == "__main__":
    main(FLAGS_CC)
