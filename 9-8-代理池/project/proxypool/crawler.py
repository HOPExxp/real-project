"""
获取模块
"""

import json
import re
from proxypool.utils import get_text
from pyquery import PyQuery as pq

class ProxyMetaclass(type):
    """
        元类，在新建的Crawler类实现特定的方法
        __CrawlFunc__和__CrawlFuncCount__两个参数
        分别表示爬虫函数，和爬虫函数的数量
    """
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

#获取模块
class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
        # self.{}()需要加(),否则只是引用方法的地址，方法并没有执行
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_text(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])