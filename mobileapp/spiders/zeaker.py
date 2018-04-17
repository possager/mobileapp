#_*_coding:utf-8_*_
from scrapy.spiders import Spider
import time
import scrapy
import pymongo
import datetime
from datetime import timedelta
import json
from mobileapp.other_module.standardization import standard
import copy





class zaker(Spider):
    name = 'zaker'



    brownser_headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
    }
    mobile_app_headers={
        'User-Agent': 'oneplus_a3010_android',
        'Host': 'app.thepaper.cn',
        'x-up-bear-type': 'WLAN',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'WDAccept-Encoding': 'gzip,deflate',
    }


    def start_requests(self):

        # def get_request_for_debug():
        #     task_list=[
        #         {
        #             'url':'http://m.thepaper.cn/channel_26916',
        #             'channelId':'channel_26916',
        #             'abstract':None,
        #             'params':None,
        #             'appname':'thepaper',
        #             'channelName':'视频'
        #         },
        #         {
        #             'url': 'http://m.thepaper.cn/channel_25953',
        #             'channelId': 'channel_25953',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'thepaper',
        #             'channelName': '生活'
        #         },
        #         {
        #             'url': 'http://m.thepaper.cn/channel_25951',
        #             'channelId': 'channel_25951',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'thepaper',
        #             'channelName': '财经'
        #         },
        #         {
        #             'url': 'http://m.thepaper.cn/channel_25950',
        #             'channelId': 'channel_25950',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'thepaper',
        #             'channelName': '时事'
        #         },
        #         {
        #             'url': 'http://m.thepaper.cn/channel_25952',
        #             'channelId': 'channel_25952',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'thepaper',
        #             'channelName': '思想'
        #         },
        #
        #     ]
        #     for one_task in task_list:
        #         yield scrapy.Request(url=one_task['url'],headers=self.brownser_headers,meta={'pre_data':one_task},callback=self.deal_board_next)
        # for i in get_request_for_debug():
        #     yield i

        client=pymongo.MongoClient('178.16.7.86',27017)
        COL=client['news']
        DOC=COL['channellist']

        mongocfg=DOC.find({'appName':'zaker','recommend':{'$gt':0}})
        for one_board in mongocfg:
            one_board_info = {
                'url': 'https://hotphone.myzaker.com/daily_hot_new.php?_appid=AndroidPhone&_bsize=720_1280&_city=%E6%88%90%E9%83%BD&_dev=1053&_lat=30.587827&_lbs_city=%E6%88%90%E9%83%BD&_lbs_province=%E5%9B%9B%E5%B7%9D%E7%9C%81&_lng=104.060447&_mac=d0%3A7a%3Ab5%3A71%3Ae8%3A9c&_mcode=FD00C81E&_net=wifi&_nudid=1b74b2323d774c39&_os=4.4.2_HUAWEIG750-T00&_os_name=HUAWEIG750-T00&_province=%E5%9B%9B%E5%B7%9D%E7%9C%81&_udid=862555023602105&_v=7.5&_version=7.5&act=pre&last_time=',
                'channelId': one_board['channelId'],
                'abstract': None,
                'params': None,
                'appname': one_board['appName'],
                'channelName': one_board['channelName']
            }
            yield scrapy.Request(url=one_board_info['url'],headers=self.brownser_headers,meta={'pre_data':one_board_info},callback=self.deal_board)
        client.close()



    def deal_board(self,response):
        '''
        :param response:

        :notice:

        '''
        metadata=response.meta['pre_data']



        board_response_json=json.loads(response.text)
        print(board_response_json)

        for one_article in board_response_json['data']['articles']:
            metadata_in_for=copy.copy(metadata)
            try:

                publish_user=one_article['auther_name']
                content=one_article['content']
                publish_time=one_article['date']
                url=one_article['url']
                _id=one_article['pk']
                title=one_article['title']
                full_url=one_article['full_url']#请求数据的api接口
            except Exception as e:
                print(e)


            one_article_dict={
                'title':title,
                'content':content,
                'publish_time':publish_time,
                'url':url,
                'id':_id,
                'publish_user':publish_user
            }

            metadata_in_for.update(one_article_dict)

            yield scrapy.Request(url=full_url,headers=self.brownser_headers,meta={'pre_data':metadata_in_for},callback=self.deal_content)





    def deal_content(self,response):
        metadata=response.meta['pre_data']
        metadata['reply_nodes']=[]


        def deal_img_urls(img_urls_raw):
            img_urls_list=[]

            for one_media in img_urls_raw:
                img_urls_list.append(one_media['raw_url'])
            return img_urls_list

        def deal_key_words(key_words_raw):
            key_words_list=[]

            for one in key_words_raw:
                key_words_list.append(one['title'])
            return key_words_list

        def deal_comment_url(_id):
            comment_url_pre='http://c.myzaker.com/weibo/api_comment_article_url.php?&pk='
            return comment_url_pre+_id



        content_response_json=json.loads(response.text)

        content=content_response_json['data']['content']
        img_urls_raw=content_response_json['data']['media']
        key_words_raw=content_response_json['data']['keywords']


        img_urls=deal_img_urls(img_urls_raw)
        key_words=deal_key_words(key_words_raw)

        article_dict={
            'content':content,
            'img_urls':img_urls,
            'params':{
                'keywords':key_words
            }
        }

        metadata.update(article_dict)

        comment_url=deal_comment_url(metadata['id'])


        return scrapy.Request(url=comment_url,headers=self.brownser_headers,meta={'pre_data':metadata},callback=self.deal_comments)



    def deal_comments(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(date,time):
            return date+' '+time

        comments_response_json=json.loads(response.text)
        for one_cmt in comments_response_json['data']['list']:
            try:
                _id=one_cmt['pk']
                publish_user_id=one_cmt['auther_pk']
                publish_user=one_cmt['auther_name']
                publish_user_photo=one_cmt['auther_icon']
                content=one_cmt['content']
                publish_time_Date=one_cmt['date']
                publish_time_Time=one_cmt['time']
            except Exception as e:
                print(e)

            publish_time=deal_publish_time(publish_time_Date,publish_time_Time)
            comments_dict={
                'id':_id,
                'publish_user_id':publish_user_id,
                'publish_user':publish_user,
                'publish_user_photo':publish_user_photo,
                'content':content,
                'publish_time':publish_time
            }
            metadata['reply_nodes'].append(comments_dict)


        next_url= comments_response_json['data']['info']['next_url']
        if next_url:
            yield scrapy.Request(url=next_url,meta={'pre_data':metadata},headers=self.brownser_headers,callback=self.deal_comments)
        else:
            yield standard(metadata)