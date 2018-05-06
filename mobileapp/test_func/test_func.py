import requests
import json



# board_dict={
#     'resource':'feed',
#     'channel':'news_ent',
#     'pullDirection':'up',
#     'pullTimes':'4',
#     'replacedFlag':'1',
#     'behavior':'manual',
#     'lastTimestamp':'1525338881',
#     'listCount':'80',
#     'upTimes':'4',
#     'downTimes':'1',
#     'localSign':'a_0f7476c9-9c78-432d-b32d-417ab8175360',
#     'todayReqTime':'0',
#     'mpName':'%E5%A8%B1%E4%B9%90',
#     'seId':'651475bd5e',
#     'deviceId':'0f6a0a591f12797b',
#     'deviceIdV1':'0f6a0a591f12797b',
#     'from':'6068495012',
#     'weiboUid':'',
#     'weiboSuid':'',
#     'imei':'865944459551126',
#     'chwm':'12030_0002',
#     'oldChwm':'12030_0002',
#     'osVersion':'5.1.1',
#     'connectionType':'2',
#     'resolution':'720x1280',
#     'city':'CHXX0016',
#     'deviceModel':'samsung__samsung__SM-G9350',
#     'location':'30.604156%2C104.060811',
#     'link':'',
#     'mac':'08%3A00%3A27%3A09%3Afe%3A9e',
#     'ua':'samsung-SM-G9350__sinanews__6.8.4__android__5.1.1',
#     'osSdk':'22',
#     'lDid':'28d1a2be-f0ec-470c-bc2d-f2399cf6e72c',
#     'accessToken':'',
#     'abt':'275_269_255_253_249_242_237_230_227_225_217_215_203_196_191_189_187_185_153_149_143_141_135_128_113_111_106_65_57_45_37_21_18_16_13',
#     'abver':'1525320808684',
#     'sn':'45956310',
#     'andId':'7003041115949825',
#     'urlSign':'75fe6dfb92',
#     'rand':'620',
# }

headers1={
    'SN-REQID':'15253388922182fc4993b6038',
    'User-Agent':'samsung-SM-G9350__sinanews__6.8.4__android__5.1.1',
    'X-User-Agent':'samsung-SM-G9350__sinanews__6.8.4__android__5.1.1',
    'Host':'newsapi.sina.cn',
    'Connection':'close'
}



request_url='http://newsapi.sina.cn/?resource=article&link=http%3A%2F%2Fent.sina.cn%2Fstar%2Fhk_tw%2F2018-05-02%2Fdetail-ifzyqqip7072195.d.html%3Fcre%3Dtianyi%26mod%3Dnent%26loc%3D6%26r%3D0%26doct%3D0%26rfunc%3D79%26tj%3Dnone%26tr%3D63%26fromsinago%3D1&newsId=fzyqqip7072195-comos-ent-cms&postt=news_news_ent_preload_null&seId=52d863ebab&deviceId=629b138f94a71410&deviceIdV1=629b138f94a71410&from=6068495012&weiboUid=&weiboSuid=&imei=865734763486949&chwm=12030_0002&oldChwm=&osVersion=5.1.1&connectionType=2&resolution=720x1280&city=CHXX0116&deviceModel=samsung__samsung__SM-G9350&location=31.247221%2C121.492479&mac=08%3A00%3A27%3A09%3Afe%3A9e&ua=samsung-SM-G9350__sinanews__6.8.4__android__5.1.1&osSdk=22&aId=01AnInoD77J-YYOqlvD9n3gW5f_7lyFqd16r6uXSPMb14bG0c.&lDid=47006e8f-bbfc-4030-89b1-05278f40d258&accessToken=&abt=276_270_255_253_249_242_237_230_227_225_217_215_207_203_196_191_189_187_157_153_149_143_141_139_135_128_113_111_57_45_38_21_18_16_13&abver=1525349203684&sn=76341321&andId=8013045295377846&urlSign=0e8449e094&rand=13'
request_url2='http://newsapi.sina.cn//?resource=feed&channel=local_shanghai&pullDirection=down&pullTimes=1&replacedFlag=0&loadingAdTimestamp=0&behavior=auto&lastTimestamp=0&listCount=0&upTimes=0&downTimes=0&localSign=a_e1432cf8-25dd-4813-a3f7-e80310a5f1d9&todayReqTime=0&mpName=%E4%B8%8A%E6%B5%B7&localCity=CHXX0116&seId=52d863ebab&deviceId=629b138f94a71410&deviceIdV1=629b138f94a71410&from=6068495012&weiboUid=&weiboSuid=&imei=865734763486949&chwm=12030_0002&oldChwm=&osVersion=5.1.1&connectionType=2&resolution=720x1280&city=CHXX0116&deviceModel=samsung__samsung__SM-G9350&location=31.247221%2C121.492479&link=&mac=08%3A00%3A27%3A09%3Afe%3A9e&ua=samsung-SM-G9350__sinanews__6.8.4__android__5.1.1&osSdk=22&aId=01AnInoD77J-YYOqlvD9n3gW5f_7lyFqd16r6uXSPMb14bG0c.&lDid=47006e8f-bbfc-4030-89b1-05278f40d258&accessToken=&abt=276_270_255_253_249_242_237_230_227_225_217_215_207_203_196_191_189_187_157_153_149_143_141_139_135_128_113_111_57_45_38_21_18_16_13&abver=1525349203684&sn=76341321&andId=8013045295377846&urlSign=1731ea2297&rand=165'


response1=requests.get(url=request_url2,headers=headers1)

print(response1.text)
datajson=response1.json()
print(datajson)
pass