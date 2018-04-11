import requests
import time
from mobileapp.other_module.execjs_cal_as_cp_for_JinRiTouTiao import caculate_as_cp



as_cp=caculate_as_cp()

headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
    'Referer':'https://m.toutiao.com/?w2atif=1&channel=news_hot',
    'Host':'m.toutiao.com',
    'Connection':'close',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept':'*/*'
}



time_str=str(int(time.time()))
url1_dict={
    'tag':'news_hot',
    'ac':'wap',
    'count':'20',
    'format':'json_raw',
    'as':as_cp['as'],
    'cp':as_cp['cp'],
    'max_behot_time':time_str,
    # '_signature':'kkyhfgAAyI04Y-H-xSTfTZJMoW',
    '_signature':time_str,
    'i':time_str
}

response1=requests.get(url='https://m.toutiao.com/list/',params=url1_dict,headers=headers)
print(response1.text)
datajson=response1.json()
print(datajson)
pass