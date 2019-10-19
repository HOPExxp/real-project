"""
redis存储模块
"""

import redis
from proxypool.error import PoolEmptyError
from proxypool.setting import REDIS_HOST,REDIS_PORT,REDIS_PW,REDIS_KEY
from proxypool.setting import MAX_SCORE,MIN_SCORE,INITAL_SCORE
from random import choice
import re

class RedisClient(object):
    def __init__(self,host = REDIS_HOST,port = REDIS_PORT,passwd = REDIS_PW):
        self.db = redis.StrictRedis(host=host,port=port,password=passwd,decode_responses=True)

    #添加单个代理--proxy
    def add(self,proxy,score = INITAL_SCORE):
        if not re.match("\d+\.\d+\.\d+\.\d+:\d+",proxy):
            print("代理不符合规范",proxy,"丢弃")
            return None
        #zscore(key, element)：返回名称为key的zset中元素element的score
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    #提供接口供用户使用
    def random(self):
        #最高分的一批代理随机选一个
        #zrangebyscore(key, min, max)：
        #返回名称为key的zset中score >= min且score <= max的所有元素
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            #随机选取位列排名前100的一个代理
            # zrevrange(key, start, end)：
            # 返回名称为key的zset（元素已按score从大到小排序）中的index从start到end的所有元素
            result = self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                #主动抛出异常
                raise PoolEmptyError

    #================================================

    #测试时调用的函数
    #下限
    def decrease(self,proxy):
        score = self.db.zscore(REDIS_KEY,proxy)
        if score and score>MIN_SCORE:
            print("代理",proxy,"当前分数",score,"减1")
            # zincrby(key, increment, member) ：
            # 如果在名称为key的zset中已经存在元素member，则该元素的score增加increment；
            # 否则向集合中添加该元素，其score的值为increment
            return self.db.zincrby(REDIS_KEY,-1,proxy)
        else:
            print("代理",proxy,"当前分数",score,"移除")
            #zrem(key, member) ：删除名称为key的zset中的元素member
            return self.db.zrem(REDIS_KEY,proxy)

    # True-存在；False-不存在
    def exists(self,proxy):
        return not self.db.zscore(REDIS_KEY,proxy) == None

    #上限
    def max(self,proxy):
        print("代理",proxy,"可用，设置为",MAX_SCORE)
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def count(self):
        # zcard(key)：返回名称为key的zset的基数
        return self.db.zcard(REDIS_KEY)

    def all(self):
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)

    #批量获取代理
    def batch(self,start,stop):
        return self.db.zrangebyscore(REDIS_KEY,start,stop-1)

if __name__ == '__main__':
    connect = RedisClient()
    result = connect.batch(1,1000)
    print(result)