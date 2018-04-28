import requests
import json
import time




xssreqticket_str=str(int(time.time()*1000))
headers1={
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9350 Build/LMY48Z) NewsArticle/6.6.6 okhttp/3.7.0.6',
            'Host': 'iu.snssdk.com',
            'Connection': 'close',
            'X-SS-REQ-TICKET': xssreqticket_str,
        }

time_str=str(int(time.time()*1000))
url1_dict={
    'group_id':'6547536226415542788',
    'item_id':'6547536226415542788',
    'aggr_type':'1',
    'count':'20',
    'offset':'40',
    'tab_index':'0',
    'fold':'1',
    # 'device_id':'51201841048',
    'iid':'30763638273',
    'ac':'wifi',
    'channel':'360',
    'aid':'13',
    'app_name':'news_article',
    'version_code':'666',
    'version_name':'6.6.6',
    'device_platform':'android',
    # 'ab_version':'264037%2C308571%2C293032%2C283773%2C320329%2C317201%2C309312%2C319438%2C317498%2C318245%2C295827%2C325050%2C315441%2C239096%2C324283%2C170988%2C318440%2C320218%2C325197%2C265169%2C281390%2C297058%2C276203%2C286212%2C313219%2C313473%2C318242%2C312563%2C310595%2C325042%2C327128%2C322322%2C327760%2C317411%2C328093%2C323233%2C304133%2C326120%2C324799%2C317076%2C324571%2C280773%2C319962%2C326729%2C317208%2C322280%2C321405%2C326342%2C214069%2C319863%2C264033%2C258356%2C247849%2C280448%2C323844%2C281299%2C320995%2C325615%2C327725%2C326807%2C328053%2C287590%2C288418%2C290192%2C260657%2C327544%2C327894%2C326190%2C327181%2C324614%2C271178%2C326589%2C326524%2C326532',
    # 'ab_client':'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7',
    # 'ab_feature':'94563%2C102749',
    'abflag':'3',
    'ssmix':'a',
    'device_type':'SM-G9350',
    'device_brand':'samsung',
    'language':'zh',
    'os_api':'22',
    'os_version':'5.1.1',
    'uuid':'865944459551126',
    # 'openudid':'7003041115949825',
    'manifest_version_code':'666',
    'resolution':'1280*720',
    'dpi':'192',
    'update_version_code':'66611',
    '_rticket':time_str,
    'plugin':'10607',
    # 'fp':'z2TqPlP_LlG7FlPrLlU1FYK7FYFI',
    # 'pos':'5r_88Pzt3vTp5L-nv3sVDXQeIHglH7-xv_zw_O3R8vP69Ono-fi_p6ytqbOtq6upqKuxv_zw_O3R_On06ej5-L-nrq2zq6yvqKyu4A%3D%3D',
    'rom_version':'22',
    'ts':'1524551666',
    'as':'a2d54ccd928ffabf3e7240',
    # 'mas':'0071fa1278a41b230146db84092b54cdcd0aa2628e8ae0c698',
    # 'odin_tt':'dc611ac46faf1607054b116a96100182592497ca4c4c7f7e2ab9d3bc5174210005f3061297bf55728f26bccaf03c0652',
    # 'qh[360]':'1',
    # 'install_id':'30763638273',
    # 'ttreq':'1$822f55234ceb355b3d20cbab3f24ec4adc299e2e',
}

while True:
    response1=requests.get(url='https://iu.snssdk.com/article/v2/tab_comments/',headers=headers1,params=url1_dict,proxies={'http':'http://14.29.47.90:3128',
                                                                                                                           'https':'https://14.29.47.90:3128'})
    print(response1.text)
    datajson=response1.json()
    print(datajson)
    if not datajson['data']:
        print('数据请求结果为空了，注意啦------------！')
    pass
    time.sleep(30)