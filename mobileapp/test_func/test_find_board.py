import requests
import json


url='http://api.hqtime.huanqiu.com/api/news/list/general/'+'comment'



headers = {
    'User-Agent': 'okhttp/3.4.1',
    'Host': 'api.hqtime.huanqiu.com',
    'content-type': 'application/json',
    'clientversion': 'v1',
    'accept': 'application/vnd.hq_time.v1+json',}

respons1=requests.get(url=url,headers=headers)
data_json=respons1.json()
print(data_json)
pass