"""
基本数据设置
"""

#redis数据库地址
REDIS_HOST = "127.0.0.1"

#reids端口
REDIS_PORT = "6379"

#redis密码，没有就设置为none
REDIS_PW = None

#代理对应的键
REDIS_KEY = "proxies"

#代理分数设置
MAX_SCORE = 100
MIN_SCORE = 0
INITAL_SCORE = 10

#状态码
STATUS_CODES = [200,302]

#代理池的界限
POOL_UPPER_LIMIT = 1000

#检查周期
CHECK_POOL = 60

#获取周期
FILL_POOL = 300

#测试网址
TEST_URL = "https://www.baidu.com"

#API配置
API_HOST = "0.0.0.0"
API_PORT = 5555

#开关配置，默认为True
TEST_ENABLED = True   #测试开关
FILL_ENABLED = True   #获取开关
API_ENABLED = True    #API开关

#最大批量测试个数
MAX_TEST_SIZE = 10