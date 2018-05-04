import requests
import json
import time


headers1={
    'Content-Encoding':'UTF-8',
    'Content-Type':'text/plain',
    'Accept':'*/*',
    'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350 Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36 JsKit/1.0 (Android)/SohuNews',
    'Authorization':'865944459551126',
    'Host':'zcache.k.sohu.com',
    'Connection':'close'
}


requests_dict={
    'p1':'NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D',
    'gid':'x011060802ff0dc5132b6d42f00069cd1e654860b7f5',
    'pid':'-1'
}


requests_dict2={
    'type':'group',
    'on':'all',
    'newsId':'271489692',
    'p1':'NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D'
}

# response1=requests.get(url='https://zcache.k.sohu.com/api/news/cdn/v5/article.go/271503531/0/0/0/3/1/12/41/3/1/1/1525401131021.json',headers=headers1,params=requests_dict)
response2=requests.get(url='https://zcache.k.sohu.com/api/share/shareon.go',params=requests_dict2,headers=headers1)


print(response2.text)
datajson=response2.json()
print(datajson)
pass