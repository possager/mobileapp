import requests


headers1={
    'User-Agent': 'okhttp/3.4.1',
    'Host': 'api.hqtime.huanqiu.com',
    'content-type': 'application/json',
    'clientversion': 'v1',
    'accept': 'application/vnd.hq_time.v1+json',}


url_list='http://api.hqtime.huanqiu.com/api/news/list/general/bigdata'

response1=requests.get(url=url_list,headers=headers1)
print(response1.text)
pass
datajson=response1.json()
print(datajson)