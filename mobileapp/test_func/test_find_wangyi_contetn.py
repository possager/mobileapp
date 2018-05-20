import requests
from scrapy.selector import Selector
import json


headers={
    'Accept-Encoding':'gzip',
    'Connection':'Keep-Alive',
    'Host':'c.m.163.com',
    'X-NR-Trace-Id':'1526809832821_50263131_863213510134567',
    'User-Agent':'NewsApp/35.1 Android/5.1.1 (samsung/SM-G9350)',
    'User-C':'5aix5LmQ',
}

response1=requests.get(url='https://c.m.163.com/nc/article/DI83U2UQ0007870A/full.html',headers=headers)
print(response1.text)