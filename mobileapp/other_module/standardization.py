#_*_coding:utf-8_*_
from mobileapp.items import MobileappItem
from datetime import datetime
import time
import hashlib
import copy




def standard(data):#将传入进来的字典标准化成item,这个组件功能可以写在pipeline中。


    #补全其它字段：publictimestamp,urlmd5（一定）/--------(不一定),user_from,channelName,channelId
    def deal_publictimestamp(data):
        if type (data['publish_time'])==type([]):
            if data['publish_time']:
                publish_time=data['publish_time'][0]
            else:
                print(data)
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

    def set_params(data):
        if 'params' in data.keys():
            if data['params']==None:
                data['params']={}
            return data
        else:
            data['params']={}
            return data

    def reSet_reply_count(data):
        try:
            if 'reply_count' not in data.keys():
                data['reply_count']=0
            data['params']['replt_count_original']=data['reply_count']
            data['reply_count']=len(data['reply_nodes'])
            return data
        except Exception as e:
            print(e)
            return data

    def deal_cmt_publictimestamp(data):
        data2=copy.copy(data)
        comment_data=data['reply_nodes']
        comment_deal_list=[]
        for oneCmt in comment_data:
            if 'publicTimestamp' not in oneCmt.keys():
                publish_time=oneCmt['publish_time']
                publicTimestamp_tuple=time.strptime(publish_time,'%Y-%m-%d %H:%M:%S')
                publicTimestamp=time.mktime(publicTimestamp_tuple)
                oneCmt['publicTimestamp']=int(publicTimestamp)

            comment_deal_list.append(oneCmt)
        data2['reply_nodes']=comment_deal_list
        return data2

    def make_comment_field_standroid(data):
        comment_list_stand = []
        for onecomment in data['reply_nodes']:
            standard_comment = standroid_comment(onecomment)
            comment_list_stand.append(standard_comment)
        data['reply_nodes'] = comment_list_stand
        return data

    data=set_params(data)
    data=reSet_reply_count(data)
    data=deal_cmt_publictimestamp(data)
    data=make_comment_field_standroid(data)


    standard_item = MobileappItem()
    for i in data.keys():
        if i in standard_item.fields:
            standard_item[i] = data[i]
    standard_item=deal_publictimestamp(standard_item)
    standard_item=deal_urlmd5(standard_item)



    return standard_item


def standroid_comment(comment_dict):
    '''
    有关publish_time和publicTimestamp的转换在spider完成，在这里将其规范化比较麻烦。
    :param comment_dict:
    :return:
    '''

    standroid_comment_dict={
        'publish_time':'',
        'publicTimestamp':'',
        'reply_nodes':[],
        'reply_count':0,
        'publish_user':'',
        'ancestor_id':'',
        'parent_id':'',
        'publish_user_id':'',
        'news_id':'',
        'like_count':0,
        'content':'',
        'publish_user_photo':'',
        'Id':'',
        'read_count':0,
        'reproduce_count':0,
        'dislike_count':0,
        'params':{}
    }

    standroid_comment_dict2={}

    for one_key in standroid_comment_dict.keys():
        if one_key not in comment_dict.keys():
            standroid_comment_dict2[one_key]=standroid_comment_dict[one_key]
        else:
            standroid_comment_dict2[one_key]=comment_dict[one_key]

    return standroid_comment_dict2

