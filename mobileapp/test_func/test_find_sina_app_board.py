import requests
import json




headers1={
    'User-Agent':'samsung-SM-G9350__sinanews__6.8.0__android__5.1.1',
    'X-User-Agent':'samsung-SM-G9350__sinanews__6.8.0__android__5.1.1',
    'Host':'newsapi.sina.cn',
    'Connection':'close'
}

url1='http://newsapi.sina.cn/?resource=feed&channel=news_ent&pullDirection=down&pullTimes=1&replacedFlag=0&loadingAdTimestamp=0&behavior=auto&lastTimestamp=0&listCount=0&upTimes=0&downTimes=0&localSign=a_e858fb0a-decf-421c-80cb-a4c22739a1cf&todayReqTime=0&mpName=%E5%A8%B1%E4%B9%90&seId=29e371d126&deviceId=0f6a0a591f12797b&from=6068095012&weiboUid=&weiboSuid=&imei=865944459551126&chwm=12030_0002&oldChwm=&osVersion=5.1.1&connectionType=2&resolution=720x1280&city=CHXX0116&deviceModel=samsung__samsung__SM-G9350&location=31.247221%2C121.492479&link=&mac=08%3A00%3A27%3A09%3Afe%3A9e&ua=samsung-SM-G9350__sinanews__6.8.0__android__5.1.1&osSdk=22&aId=01AhmBqbS_paGtZVj9KbfkBrLsTB2s0fjkwsEqzPmxKioNkf0.&lDid=28d1a2be-f0ec-470c-bc2d-f2399cf6e72c&accessToken=&abt=253_242_237_230_227_225_215_203_196_191_189_187_185_153_149_143_141_135_128_113_111_106_101_99_65_57_45_37_21_18_16_13&abver=1524103219680&urlSign=3d4d65d1c9&rand=108'
url2='http://newsapi.sina.cn/?resource=feed&channel=news_ent&pullDirection=down&pullTimes=1&replacedFlag=0&loadingAdTimestamp=0&behavior=auto&lastTimestamp=0&listCount=0&upTimes=0&downTimes=0&localSign=a_e858fb0a-decf-421c-80cb-a4c22739a1cf&todayReqTime=0&mpName=%E5%A8%B1%E4%B9%90&seId=29e371d126&deviceId=0f6a0a591f12797b&from=6068095012&weiboUid=&weiboSuid=&imei=865944459551126&chwm=12030_0002&oldChwm=&osVersion=5.1.1&connectionType=2&resolution=720x1280&city=CHXX0116&deviceModel=samsung__samsung__SM-G9350&location=31.247221%2C121.492479&link=&mac=08%3A00%3A27%3A09%3Afe%3A9e&ua=samsung-SM-G9350__sinanews__6.8.0__android__5.1.1&osSdk=22&aId=01AhmBqbS_paGtZVj9KbfkBrLsTB2s0fjkwsEqzPmxKioNkf0.&lDid=28d1a2be-f0ec-470c-bc2d-f2399cf6e72c&accessToken=&abt=253_242_237_230_227_225_215_203_196_191_189_187_185_153_149_143_141_135_128_113_111_106_101_99_65_57_45_37_21_18_16_13&abver=1524103219680&urlSign=3d4d65d1c9&rand=108'
url3='http://newsapi.sina.cn/?resource=article&link=http%3A%2F%2Fnews.sina.cn%2F2018-04-13%2Fdetail-ifzcyxmu0277344.d.html%3Ffromsinago%3D1&newsId=fzcyxmu0277344-comos-news-cms&postt=news_news_shijiuda_preload_null&seId=29e371d126&deviceId=0f6a0a591f12797b&from=6068095012&weiboUid=&weiboSuid=&imei=865944459551126&chwm=12030_0002&oldChwm=&osVersion=5.1.1&connectionType=2&resolution=720x1280&city=CHXX0116&deviceModel=samsung__samsung__SM-G9350&location=31.247221%2C121.492479&mac=08%3A00%3A27%3A09%3Afe%3A9e&ua=samsung-SM-G9350__sinanews__6.8.0__android__5.1.1&osSdk=22&aId=01AhmBqbS_paGtZVj9KbfkBrLsTB2s0fjkwsEqzPmxKioNkf0.&lDid=28d1a2be-f0ec-470c-bc2d-f2399cf6e72c&accessToken=&abt=253_242_237_230_227_225_215_203_196_191_189_187_185_153_149_143_141_135_128_113_111_106_101_99_65_57_45_37_21_18_16_13&abver=1524103219680&urlSign=b2a8fd757b&rand=709'
url4='http://newsapi.sina.cn/?resource=hbpage&newsId=HB-1-secf%2Findex-downfloor&link=&page=1&seId=29e371d126&deviceId=0f6a0a591f12797b&from=6068095012&weiboUid=&weiboSuid=&imei=865944459551126&chwm=12030_0002&oldChwm=&osVersion=5.1.1&connectionType=2&resolution=720x1280&city=CHXX0116&deviceModel=samsung__samsung__SM-G9350&location=31.247221%2C121.492479&mac=08%3A00%3A27%3A09%3Afe%3A9e&ua=samsung-SM-G9350__sinanews__6.8.0__android__5.1.1&osSdk=22&aId=01AhmBqbS_paGtZVj9KbfkBrLsTB2s0fjkwsEqzPmxKioNkf0.&lDid=28d1a2be-f0ec-470c-bc2d-f2399cf6e72c&accessToken=&abt=253_242_237_230_227_225_215_203_196_191_189_187_185_153_149_143_141_135_128_113_111_106_101_99_65_57_45_37_21_18_16_13&abver=1524103219680&urlSign=1252c5d7d3&rand=145'



response1=requests.get(url=url4,headers=headers1)
print(response1.text)
datajson=response1.json()

pass