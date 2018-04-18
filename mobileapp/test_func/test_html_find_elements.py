import requests
import json



host='wx.qlogo.cn'
url1='http://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIalruficibMEEfRV1V4ZdjYVuibBqpiaJVNaDWFJibNJgJ34eyCNcuKvQJknQYXjVvzpd1AwZmxjnIqAA/132'
url2='http://cc.contx.cn/cclick?accessId=50001&articleIds=15239225422331843&rpid=&vid=15155081&articlesId=&magId=&installversion=7.0.6'
url3='http://182.150.10.51/gchatpic_new/C69483DBBB6CCB3E084469D2325AEE47AD1E058CF6EB781C01510AD25B4EBA20FB01EFC2D807275833598FD8EF6967EBE3FFC845D65CB3F7892012F30EC852450BDA07F3AB7A7202A5526BCF93474749DBEBDECFA2FA8ACF/0?vuin=850629192&term=1&srvver=26769&rf=naio'



headers1={
    'Cache-Control':'max-age=2592000',
    'X-Delay':'494 us',
    'X-Info':'real data',
    'X-BCheck':'0_1',
    'X-Cpt':'filename=0',
    'User-ReturnCode':'0',
    'X-DataSrc':'0',
    'X-ReqGue':'0',
    'Size':'6339',
    'chid':'0',
    'fid':'0'
}



response1=requests.get(url=url3,headers=headers1)
print(response1.text)

with open('E:/scrapy_data2/tests','wb') as fl:
    fl.write(response1.content)