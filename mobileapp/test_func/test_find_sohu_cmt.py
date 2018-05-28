import requests
import json



url1='https://api.k.sohu.com/api/comment/getCommentListByCursor.go'

params1={
    'busiCode':'2',
    'apiVersion':'41',
    'channelId':'1',
    'cursorId':'',
    # 'from':'1527217578021',
    # 'gid':'x011060802ff0dc5132b6d42f00069cd1e654860b7f5',
    'id':'275219836',#275871211
    'openType':'',
    # 'p1':'NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D',
    'u':'1',
    'page':'1',
    'pid':'-1',
    'position':'4',
    'refer':'3',
    'rollType':'1',
    'rt':'json',
    'size':'10',
    'source':'news',
    'subId':'130152',
    'type':'5',
    'refererType':'',
    'articleDebug':'0',
}

params2={'busiCode': '2', 'apiVersion': '41', 'channelId': '1', 'cursorId': '', 'id': '275888671', 'openType': '', 'u': '1', 'page': '1', 'pid': '-1', 'position': '4', 'refer': '3', 'rollType': '1', 'rt': 'json', 'size': '10', 'source': 'news', 'subId': '130152', 'type': '5', 'refererType': '', 'articleDebug': ''}

headers1={
    'Connection':'close',
    'Accept':'*/*',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350 Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36 JsKit/1.0 (Android);',
}

response1=requests.get(url=url1,headers=headers1,params=params2)

print(response1.text)

datajson=json.loads(response1.text)
print(datajson)