"""
获取网页源码
"""

import requests
from requests.exceptions import ConnectionError
from fake_useragent import UserAgent

def get_text(url,options = {}):
    ua = UserAgent().chrome
    headers = {
        "User-Agent":ua
    }
    print("正在抓取",url)
    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        print("抓取成功",url)
        r.encoding = r.apparent_encoding
        return r.text
    except ConnectionError:
        print("抓取失败",url)
        return None