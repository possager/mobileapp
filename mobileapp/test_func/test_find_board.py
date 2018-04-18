import requests
import json

article_id='15238706517293165'
url='http://interfacev5.vivame.cn/x1-interface-v5/json/commentlist.json?platform=android&installversion=6.2.2.2&channelno=AZWMA2320480100&mid=5284047f4ffb4e04824a2fd1d1f0cd62&uid=3125&sid=f4umcvbs-4154-495a-b13f-2245a758834a&type=0&id='+article_id+'&pageindex=0&pagesize=20&commentType=4'
url2='http://cc.contx.cn/cclick?accessId=50001&articleIds=15238772966011757&rpid=&vid=15154713&articlesId=&magId=&installversion=7.0.6'



headers1={
            "Connection": "Keep-Alive",
            "Host": "interfacev5.vivame.cn",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "AcceptEncoding": "gzip, deflate",
            "Cache-Control": "max-age=0",
            "Connecttion": "keep-alive"
            }

response1=requests.get(url=url,headers=headers1)
print(response1.text)
datajson=response1.json()
print(datajson)
pass