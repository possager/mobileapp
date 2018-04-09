import requests


url1='http://opinion.huanqiu.com/opinion_china/2018-04/11768748.html'

headers={
    'User-Agent': 'okhttp/3.4.1',
    'Host': 'api.hqtime.huanqiu.com',
    'content-type': 'application/json',
    'clientversion': 'v1',
    'accept': 'application/vnd.hq_time.v1+json'
}

reposnse1=requests.get(url=url1)
print(reposnse1.text)