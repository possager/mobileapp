#_*_coding:utf-8_*_
from mobileapp.items import MobileappItem
from datetime import datetime
import time
import hashlib




def standard(data):#将传入进来的字典标准化成item
    standard_item=MobileappItem()
    for i in data.keys():
        if i in standard_item.fields:
            standard_item[i]=data[i]

    #补全其它字段：publictimestamp,urlmd5（一定）/--------(不一定),user_from,channelName,channelId
    def deal_publictimestamp(data):
        if type (data['publish_time'])==type([]):
            if data['publish_time']:
                publish_time=data['publish_time'][0]
            else:
                data['publish_time']='1111-11-11 11:11:11'
                return data
        else:
            publish_time=data['publish_time']

        try:
            time_tuple=time.strptime(publish_time,'%Y-%m-%d %H:%M:%S')
            timestamp=int(time.mktime(time_tuple))

            data['publicTimestamp']=timestamp
        except Exception as e:
            print(e)
            print(data['publish_time'])
        return data

    def deal_urlmd5(data):
        url=data['url']
        urlmd5=hashlib.md5(str(url).encode('utf-8')).hexdigest()

        data['urlmd5']=urlmd5
        return data


    standard_item=deal_publictimestamp(standard_item)
    standard_item=deal_urlmd5(standard_item)



    return standard_item