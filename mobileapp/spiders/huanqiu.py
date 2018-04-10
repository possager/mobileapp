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
from urllib.parse import quote




class huanqiu(Spider):
    name = 'huanqiu'



    brownser_headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        'Upgrade-Insecure-Requests':'1',
        'Host':'commentn.huanqiu.com',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
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
            for one_task in task_list[:2]:
                yield scrapy.Request(url=one_task['url'],headers=self.mobile_app_headers,meta={'pre_data':one_task},callback=self.deal_board)
        for i in get_request_for_debug():
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
                try:
                    reply_count=one_article['comment_count']
                except Exception as e:
                    reply_count=0
                like_count=one_article['like_amount']
                source=one_article['source']
                abstract=one_article['summary']
                publicTimestamp=one_article['time_publish']
                title=one_article['title']
                url=one_article['url']
                comment_source_id=one_article['comment_source_id']



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
                    'comment_source_id':comment_source_id
                }
                metadata_in_for.update(article_dict)

                yield scrapy.Request(url=url,meta={'pre_data':metadata_in_for},callback=self.deal_content)


    def deal_content(self,response):
        metadata=response.meta['pre_data']


        def deal_comment_url(data_meta):
            comment_source_id=data_meta['comment_source_id']
            url1='https://commentn.huanqiu.com/api/v2/async?&a=comment&m=source_info&appid=e8fcff106c8f&sourceid='+str(comment_source_id)
            url_quote=quote(data_meta['url'])

            url1=url1+'&url='+url_quote
            return url1




        content=response.xpath('//div[@class="content_wrap"]').extract_first(default=None)
        img_urls=response.xpath('//div[@class="content_wrap"]//img/@src').extract()


        content_dict={
            'content':content,
            'img_urls':img_urls,
            'reply_nodes':[]
        }
        metadata.update(content_dict)


        url_for_commentId=deal_comment_url(metadata)

        yield scrapy.Request(url=url_for_commentId,headers=self.brownser_headers,meta={'pre_data':metadata},callback=self.deal_comment_url_Next)


    def deal_comment_url_Next(self,response):
        metadata=response.meta['pre_data']


        def deal_url_for_Comment(data_json):
            comment_id = data_json['data']['_id']
            url_for_Comment = 'https://commentn.huanqiu.com/api/v2/async?&a=comment&m=comment_list&appid=e8fcff106c8f&sid=' + comment_id + '&n=10&p=1'
            return url_for_Comment

        datajson=json.loads(response.text)

        url_for_Comment=deal_url_for_Comment(datajson)
        yield scrapy.Request(url=url_for_Comment, headers=self.brownser_headers, meta={'pre_data': metadata},
                             callback=self.deal_comments)


    def deal_comments(self,response):
        metadata=response.meta['pre_data']


        def deal_commentUrl_next(comment_url):
            commentUrl_split=comment_url.split('&p=')
            pageNum=int(commentUrl_split[1])
            url_pre=commentUrl_split[0]


            return url_pre+'&p='+str(pageNum+1)


        comment_response_json=json.loads(response.text)

        #处理评论
        if comment_response_json['msg']=='success':#空则为'empty',这种情况很少
            for one_comment in comment_response_json['data']:
                _id=one_comment['_id']
                content=one_comment['content']
                publicTimestamp=one_comment['ctime']
                ip=one_comment['ip']
                address=one_comment['loc']
                publish_user_id=one_comment['user']['uid']
                publish_user_photo=one_comment['user']['avatar']
                publish_user=one_comment['user']['nickname']
                source=one_comment['user']['source']

                one_comment_dict={
                    'id':_id,
                    'content':content,
                    'publicTimestamp':publicTimestamp,
                    'params':{
                        'ip':ip,
                        'address':address,
                        'source':source
                    },
                    'publish_user_id':publish_user_id,
                    'publish_user_photo':publish_user_photo,
                    'publish_user':publish_user,
                    'parent_id':metadata['id'],
                    'ancestor_id':metadata['id']
                }
                metadata['reply_nodes'].append(one_comment_dict)
        else:
            return standard(metadata)


        #决定是否需要继续请求评论
        if len(comment_response_json['data'])==10:
            commenturlNext=deal_commentUrl_next(response.url)
            return scrapy.Request(url=commenturlNext,headers=self.brownser_headers,callback=self.deal_comments,meta={'pre_data':metadata})
        else:
            return standard(metadata)