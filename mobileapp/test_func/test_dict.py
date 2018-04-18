import requests


headers1={
    "Connection": "Keep-Alive",
    "Host": "interfacev5.vivame.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "AcceptEncoding": "gzip, deflate",
    "Cache-Control": "max-age=0",
    "Connecttion": "keep-alive",
}

data_dict={
    "platform": "android",
    "installversion": "6.7.0.1",
    "channelno": "MZSDA2320480100",
    "mid": "cb8de243d6ca911fc673ab4bab1dfecd",
    "uid": "14400699",
    "sid": "75ip2pfj-32j8-nebk-kec5-ed61b7956312",
    "type":"1",
    "category": "1",
    "ot": "0",
    "nt": "0"
    }




url_list='http://interfacev5.vivame.cn/x1-interface-v5/json/newdatalist.json?id='

data_dict['id']='156'


response1=requests.post(url='http://interfacev5.vivame.cn/x1-interface-v5/json/newdatalist.json',headers=headers1,data=data_dict)
print(response1.text)
pass
datajson=response1.json()
print(datajson)