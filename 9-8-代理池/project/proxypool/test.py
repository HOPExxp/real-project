import re

r = """192.168.1.1:2000
192.168.0.0:3000"""

t = re.findall("\d+\.\d+\.\d+\.\d+\:\d+",r)
print(t)
