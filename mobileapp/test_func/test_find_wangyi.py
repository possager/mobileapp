import requests
from scrapy.selector import Selector
import json



url1='/recommend/getSubDocPic?tid=T1348647909107&from=toutiao&offset=20&size=10&fn=1&LastStdTime=1526756888&spestr=shortnews&prog=&passport=&devId=iBqHGWB8Yx8XkfAf9bTKRw%3D%3D&lat=&lon=&version=35.1&net=wifi&ts=1526773568&sign=Kr8H5%2FefevcqnpXLD6j4pyk%2FQKy7LsH5M0sslXNj5g148ErR02zJ6%2FKXOnxX046I&encryption=1&canal=news_lljc3&mac=Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30%3D&open=&openpath='
host='http://c.m.163.com'

url3='http://c.m.163.com/recommend/getSubDocPic'

params={
    'tid':'T1348647909107',
    'from':'toutiao',
    'offset':'20',
    'size':'10',
    'fn':'1',
    'LastStdTime':'1526756888',
    'spestr':'shortnews',
    'prog':'',
    # 'passport':'',
    'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
    # 'lat':'',
    # 'lon':'',
    # 'version':'35.1',
    # 'net':'wifi',
    # 'ts':'1526773568',
    # 'sign':'Kr8H5/efevcqnpXLD6j4pyk/QKy7LsH5M0sslXNj5g148ErR02zJ6/KXOnxX046I',
    # 'encryption':'1',
    'canal':'news_lljc3',
    # 'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
    # 'open':'',
    # 'openpath':''
}


params_shipin={
            'channel':'T1457068979049',
            'subtab':'Video_Recom',
            'size':'10',
            'offset':'0',
            'fn':'1',
            'passport':'',
            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
            'lat':'',
            'lon':'',
            'version':'35.1',
            'net':'wifi',
            # 'ts':'1526776833',
            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
            # 'encryption':'1',
            # 'canal':'news_lljc3',
            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
            'open':'',
            'openpath':''
        }

params_caijing={
            'from':'T1348648756099',
            'size':'10',
            'offset':'0',
            'fn':'1',
            'passport':'',
            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
            'lat':'',
            'lon':'',
            'version':'35.1',
            'net':'wifi',
            # 'ts':'1526776833',
            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
            # 'encryption':'1',
            # 'canal':'news_lljc3',
            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
            'open':'',
            'openpath':''
        }

params_keji={
            'from':'T1348649580692',
            'size':'10',
            'offset':'0',
            'fn':'1',
            'passport':'',
            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
            'lat':'',
            'lon':'',
            'version':'35.1',
            'net':'wifi',
            # 'ts':'1526776833',
            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
            # 'encryption':'1',
            # 'canal':'news_lljc3',
            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
            'open':'',
            'openpath':''
        }

params_yaowen={
            'from':'T1467284926140',
            'size':'10',
            'offset':'0',
            'fn':'1',
            'passport':'',
            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
            'lat':'',
            'lon':'',
            'version':'35.1',
            'net':'wifi',
            # 'ts':'1526776833',
            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
            # 'encryption':'1',
            # 'canal':'news_lljc3',
            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
            'open':'',
            'openpath':''
        }

params_yaowen={
            'from':'T1467284926140',
            'size':'10',
            'offset':'0',
            'fn':'1',
            'passport':'',
            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
            'lat':'',
            'lon':'',
            'version':'35.1',
            'net':'wifi',
            # 'ts':'1526776833',
            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
            # 'encryption':'1',
            # 'canal':'news_lljc3',
            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
            'open':'',
            'openpath':''
        }

params_junshi={
            'from':'T1348648141035',
            'size':'10',
            'offset':'0',
            'fn':'1',
            'passport':'',
            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
            'lat':'',
            'lon':'',
            'version':'35.1',
            'net':'wifi',
            # 'ts':'1526776833',
            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
            # 'encryption':'1',
            # 'canal':'news_lljc3',
            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
            'open':'',
            'openpath':''
        }



url2=host+url1

headers={
    'X-NR-Trace-Id': '1526773568760_1035271646_863213510134567',
    'User-N': 'wKq3+ZhKJshqLUdmuO/3GU54yPhI0ZGYXNBL+qbp+gYtkyOvjJ64oHfDp3tOH9cB',
    'User-D': 'iBqHGWB8Yx8XkfAf9bTKRw==',
    'User-C': '5aS05p2h',
    'httpDNSIP': '59.111.160.220',
    'data4-Sent-Millis': '1526773568759',
    'Add-To-Queue-Millis': '1526773568748',
    'User-Agent': 'NewsApp/35.1 Android/5.1.1 (samsung/SM-G9350)',
    'Accept-Encoding': 'gzip'
}

# response1=requests.get(url=url2,headers=headers)

response1=requests.get(url=url3,params=params_keji,headers=headers)

selector1=Selector(text=response1.text)
print(response1.text)