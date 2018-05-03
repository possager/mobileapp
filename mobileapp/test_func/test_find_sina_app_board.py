import requests
import json




headers1={
    # 'GET':'/?resource=comment/baseInfo&commentId=comos-fyuwqfa5260849_0_sh__fyuwqfa5260849-comos-news-cms&postt=news_null_null_push_gexin&page=2&seId=651475bd5e&deviceId=0f6a0a591f12797b&deviceIdV1=0f6a0a591f12797b&from=6068495012&weiboUid=&weiboSuid=&imei=865944459551126&chwm=12030_0002&oldChwm=12030_0002&osVersion=5.1.1&connectionType=2&resolution=720x1280&city=CHXX0016&deviceModel=samsung__samsung__SM-G9350&location=30.604156%2C104.060811&link=&mac=08%3A00%3A27%3A09%3Afe%3A9e&ua=samsung-SM-G9350__sinanews__6.8.4__android__5.1.1&osSdk=22&aId=01AhmBqbS_paGtZVj9KbfkBrKBWizdzGleDcmoNBxiPRsmSA0.&lDid=28d1a2be-f0ec-470c-bc2d-f2399cf6e72c&accessToken=&abt=275_269_255_253_249_242_237_230_227_225_217_215_203_196_191_189_187_185_153_149_143_141_135_128_113_111_106_65_57_45_37_21_18_16_13&abver=1525320808684&sn=45956310&andId=7003041115949825&urlSign=81a6a5021e&rand=330 HTTP/1.1',
    'User-Agent':'samsung-SM-G9350__sinanews__6.8.0__android__5.1.1',
    'X-User-Agent':'samsung-SM-G9350__sinanews__6.8.0__android__5.1.1',
    'Host':'newsapi.sina.cn',
    'Connection':'close',
    'SN-REQID':'15253365507892fc4993b8622'
}

data_get_comment_dict={
    'resource':'comment/baseInfo',
    'commentId':'comos-fyuwqfa5260849_0_sh__fyuwqfa5260849-comos-news-cms',
    'postt':'news_null_null_push_gexin',
    'page':'2',
    'seId':'651475bd5e',
    'deviceId':'0f6a0a591f12797b',
    'deviceIdV1':'0f6a0a591f12797b',
    'from':'6068495012',
    'weiboUid':'',
    'weiboSuid':'',
    'imei':'865944459551126',
    'chwm':'12030_0002',
    'oldChwm':'12030_0002',
    'osVersion':'5.1.1',
    'connectionType':'2',
    'resolution':'720x1280',
    'city':'CHXX0016',
    'deviceModel':'samsung__samsung__SM-G9350',
    'location':'30.604156%2C104.060811',
    'link':'',
    'mac':'08%3A00%3A27%3A09%3Afe%3A9e',
    'ua':'samsung-SM-G9350__sinanews__6.8.4__android__5.1.1',
    'osSdk':'22',
    'aId':'01AhmBqbS_paGtZVj9KbfkBrKBWizdzGleDcmoNBxiPRsmSA0.',
    'lDid':'28d1a2be-f0ec-470c-bc2d-f2399cf6e72c',
    'accessToken':'',
    'abt':'275_269_255_253_249_242_237_230_227_225_217_215_203_196_191_189_187_185_153_149_143_141_135_128_113_111_106_65_57_45_37_21_18_16_13',
    'abver':'1525320808684',
    'sn':'45956310',
    'andId':'7003041115949825',
    'urlSign':'81a6a5021e',
    # 'rand':'330',
}


response1=requests.get(url='http://newsapi.sina.cn',headers=headers1,params=data_get_comment_dict)
print(response1.text)