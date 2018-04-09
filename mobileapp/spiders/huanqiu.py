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





class huanqiu(Spider):
    name = 'huanqiu'



    brownser_headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
    }
    mobile_app_headers={
    'User-Agent': 'okhttp/3.4.1',
    'Host': 'api.hqtime.huanqiu.com',
    'content-type': 'application/json',
    'clientversion': 'v1',
    'accept': 'application/vnd.hq_time.v1+json',}


    def start_requests(self):

        def get_request_for_debug():
            task_list=[
                {
                    'url':'http://api.hqtime.huanqiu.com/api/news/list/general/comment',
                    'channelId':'comment',
                    'abstract':None,
                    'params':None,
                    'appname':'huanqiu',
                    'channelName':'评论'
                },
                {
                    'url': 'http://api.hqtime.huanqiu.com/api/news/list/general/international',
                    'channelId': 'international',
                    'abstract': None,
                    'params': None,
                    'appname': 'huanqiu',
                    'channelName': '国际'
                },
                {
                    'url': 'http://api.hqtime.huanqiu.com/api/news/list/general/taihai',
                    'channelId': 'taihai',
                    'abstract': None,
                    'params': None,
                    'appname': 'huanqiu',
                    'channelName': '台海'
                },
                {
                    'url': 'http://api.hqtime.huanqiu.com/api/news/list/general/internal',
                    'channelId': 'internal',
                    'abstract': None,
                    'params': None,
                    'appname': 'huanqiu',
                    'channelName': '国内'
                },
                {
                    'url': 'http://api.hqtime.huanqiu.com/api/news/list/general/military',
                    'channelId': 'military',
                    'abstract': None,
                    'params': None,
                    'appname': 'huanqiu',
                    'channelName': '军事'
                },

            ]
            for one_task in task_list:
                yield scrapy.Request(url=one_task['url'],headers=self.brownser_headers,meta={'pre_data':one_task},callback=self.deal_board)
        for i in get_request_for_debug()[:1]:
            yield i

        # client=pymongo.MongoClient('178.16.7.86',27017)
        # COL=client['news']
        # DOC=COL['channellist']
        #
        # mongocfg=DOC.find({'appName':'thepaper','recommend':{'$gt':0}})
        # for one_board in mongocfg:
        #     one_board_info = {
        #         'url': one_board['url'],
        #         'channelId': one_board['channelId'],
        #         'abstract': None,
        #         'params': None,
        #         'appname': 'thepaper',
        #         'channelName': one_board['channelName']
        #     }
        #     yield scrapy.Request(url=one_board['url'],headers=self.brownser_headers,meta={'pre_data':one_board_info},callback=self.deal_board_next)
        # client.close()



    def deal_board(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publicTimestamp):
            publicTimestamp_int=int(publicTimestamp)
            time_tuple=time.localtime(publicTimestamp_int)
            publish_time_in_func=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
            return publish_time_in_func


        board_response_json=json.loads(response.text)
        for one_article_collection in board_response_json['data']:
            for one_article in one_article_collection['group_data']:
                metadata_in_for=copy.copy(metadata)

                _id=one_article['id']
                publish_user=one_article['editor']
                reply_count=one_article['commment_count']
                like_count=one_article['like_amount']
                source=one_article['source']
                abstract=one_article['summary']
                publicTimestamp=one_article['time_publish']
                title=one_article['title']
                url=one_article['url']


                publish_time=deal_publish_time(publicTimestamp)

                article_dict={
                    'id':_id,
                    'publish_user':publish_user,
                    'reply_count':reply_count,
                    'like_count':like_count,
                    'source':source,
                    'abstract':abstract,
                    'publicTimestamp':publicTimestamp,
                    'title':title,
                    'url':url,
                    'publish_time':publish_time,
                }
                metadata_in_for.update(article_dict)

                yield scrapy.Request(url=url,meta={'pre_data':metadata_in_for},callback=self.deal_content)





    def deal_content(self,response):
        metadata=response.meta['pre_data']


        def deal_content(content_raw):
            if content_raw:
                
                content_str=content_raw


        content=response.xpath('//div[@class="content"]/p//text()').extract()
        img_urls=response.xpath('//div[@class="content"]//img/@src').extract()







    def deal_comments(self,response):
        metadata=response.meta['pre_data']
        formdata=response.meta['formdata']