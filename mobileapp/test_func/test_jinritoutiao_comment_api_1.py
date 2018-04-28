import requests
import time


xssreqticket_str=str(int(time.time()*1000))
headers1={
'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9350 Build/LMY48Z) NewsArticle/6.6.6 okhttp/3.7.0.6',
            'Host': 'iu.snssdk.com',
            'Connection': 'close',
            'X-SS-REQ-TICKET': xssreqticket_str,
}

headers2={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Connection':'keep-alive',
    'Accept-Language':'zh-CN,zh;q=0.9'
}


while True:

    response1=requests.get(url='https://www.toutiao.com/api/comment/list/?group_id=6547536226415542788&item_id=6547536226415542788&offset=0&count=10',headers=headers2)
    print(response1.text)
    datajson=response1.json()
    print(datajson)
    if not datajson['data']:
        print('data的数据已经是空了，注意啦！')
    time.sleep(30)