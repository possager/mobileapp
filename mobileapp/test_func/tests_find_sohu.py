import requests
import json
import time



headers1={
    'STM':'1525399145234',
    'SNONCE':"1977539389",
    'SCOOKIEV2':'7XmaWntDsPhAEdmVUN/Ip6+wbE31Gd8vRZ5/R6VJbbq2WCGhAW8Ppcmps+K7jvOi0uW7tgusa6QiP6y5VnVOu99Ne9fzzc+Uwir/6UmQ97ajRMo2ePyKLgDJJsAaYDyWqlJL85AjvRb3260UiuqOR2vX48gXmZFUMwymhOnxGoA8992IttsmC+MuyXzrPlu7g/VoTJRn4uXCxoxPI8hkBdWBoad0jZpI1OguKsDsw/Jjxs1usyVyX22iry4ljNMH7aPaSVUHdhsth/sYAS9qTqfjmFkZ2iRjgnWYjH6p9KKKGkU/oSrv5hnp5bZbvx7UK6JAXEPWz+6GgW7borhi+icPnQ2Atj7OsZWxN4qm3EW1e+1+OUhhHG1SKGeIL2sf',
    'REQID':'4b465683e2434666bbb71a62f8cc484d',
    'SSIG':'85e96ccdd1ece817a737017a19c136b0',
    'SVER':'1517381440|',
    'Host':'api.k.sohu.com',
    'Connection':'close',
    'User-Agent':'okhttp/3.9.1'
}

request_data={
    'p1':'NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D',
    'pid':'-1',
    'channelId':'1',
    'num':'20',
    'imgTag':'1',
    'showPic':'1',
    'picScale':'11',
    'rt':'json',
    'net':'wifi',
    # 'cdma_lat':'30.613886',
    # 'cdma_lng':'104.064753',
    'from':'channel',
    # 'mac':'08%3A00%3A27%3A09%3Afe%3A9e',
    # 'AndroidID':'7003041115949825',
    # 'carrier':'China+Mobile+GSM',
    # 'imei':'865944459551126',
    # 'imsi':'460006310769711',
    # 'density':'1.2',
    # 'apiVersion':'41',
    # 'isMixStream':'0',
    # 'skd':'3b879454c81309ede513df29aaf931f04b42cbf30c5dc8802680568953e97cb8547587596446ec4f9ba2a7be341a7bf45cb3bb2596b81af80e292e0bc8cc0781249bee10caf24addf9eed1bb7f27e06a3444ad3ef89d79031848b88598d735f1a8afffda780d1129d139af0c8abdea2b',
    'v':'1525363200',
    # 't':'1525399145',
    'forceRefresh':'1',
    'times':'0',
    'page':'1',
    'action':'0',
    'mode':'0',
    'cursor':'0',
    'mainFocalId':'0',
    'focusPosition':'1',
    'viceFocalId':'0',
    'lastUpdateTime':'0',
    # 'gbcode':'510100',
    'u':'1',
    'source':'0',
    'actiontype':'1',
    # 'isSupportRedPacket':'0',
    # 't':'1525399145',
    # 'rr':'1',

}


response1=requests.get(url='https://api.k.sohu.com/api/channel/v6/news.go',params=request_data,headers=headers1)
# response1=requests.get(url='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D&pid=-1&channelId=1&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=30.613886&cdma_lng=104.064753&from=channel&mac=08%3A00%3A27%3A09%3Afe%3A9e&AndroidID=7003041115949825&carrier=China+Mobile+GSM&imei=865944459551126&imsi=460006310769711&density=1.2&apiVersion=41&isMixStream=0&skd=3b879454c81309ede513df29aaf931f04b42cbf30c5dc8802680568953e97cb8547587596446ec4f9ba2a7be341a7bf45cb3bb2596b81af80e292e0bc8cc0781249bee10caf24addf9eed1bb7f27e06a3444ad3ef89d79031848b88598d735f1a8afffda780d1129d139af0c8abdea2b&v=1525363200&t=1525399145&forceRefresh=1&times=0&page=1&action=0&mode=0&cursor=0&mainFocalId=0&focusPosition=1&viceFocalId=0&lastUpdateTime=0&gbcode=510100&apiVersion=41&u=1&source=0&actiontype=1&isSupportRedPacket=0&t=1525399145&rr=1')
print(response1.text)
datajson=response1.json()
print(datajson)
pass
