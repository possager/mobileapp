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
import re
from urllib.parse import unquote




class jiemian(Spider):
    name = 'jiemian'



    brownser_headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
    }
    mobile_app_headers={
        'User-Agent': 'JiemianNews/5.1.0 (android; android 4.4.4; ONEPLUS A3010)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'appapi.jiemian.com',
        'Connection': 'close'
    }


    def start_requests(self):

        # def get_request_for_debug():
        #     task_list=[
        #         {
        #             'url':'http://appapi.jiemian.com/v4/5.1.0/10001/cate/117/0/1/51/5101.json?vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI',
        #             'channelId':'117',
        #             'abstract':None,
        #             'params':None,
        #             'appname':'JieMianXinWen',
        #             'channelName':'商业'
        #         },
        #         {
        #             'url': 'http://appapi.jiemian.com/v4/5.1.0/10001/cate/643/0/1/51/5101.json?vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI',
        #             'channelId': '643',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'JieMianXinWen',
        #             'channelName': '财经'
        #         },
        #         {
        #             'url': 'http://appapi.jiemian.com/v4/5.1.0/10001/cate/644/0/1/51/5101.json?vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI',
        #             'channelId': '644',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'JieMianXinWen',
        #             'channelName': '新闻'
        #         },
        #         {
        #             'url': 'http://appapi.jiemian.com/v4/5.1.0/10001/cate/123/0/1/51/5101.json?vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI',
        #             'channelId': '123',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'JieMianXinWen',
        #             'channelName': '科技'
        #         },
        #         {
        #             'url': 'http://appapi.jiemian.com/v4/5.1.0/10001/cate/138/0/1/51/5101.json?vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI',
        #             'channelId': '138',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'JieMianXinWen',
        #             'channelName': '汽车'
        #         },
        #
        #     ]
        #     for one_task in task_list:
        #         yield scrapy.Request(url=one_task['url'],headers=self.mobile_app_headers,meta={'pre_data':one_task},callback=self.deal_board)
        # for i in get_request_for_debug():
        #     yield i

        client=pymongo.MongoClient('178.16.7.86',27017)
        COL=client['news']
        DOC=COL['channellist']

        mongocfg=DOC.find({'appName':'JieMianXinWen','recommend':{'$gt':0}})
        for one_board in mongocfg:
            one_board_info = {
                'url': one_board['url'],
                'channelId': one_board['channelId'],
                'abstract': None,
                'params': None,
                'appname': 'thepaper',
                'channelName': one_board['channelName']
            }
            yield scrapy.Request(url=one_board['url'],headers=self.mobile_app_headers,meta={'pre_data':one_board_info},callback=self.deal_board)
        client.close()



    def deal_board(self,response):
        metadata=response.meta['pre_data']


        def deal_reply_count(reply_count_raw):
            if 'w' in reply_count_raw:
                reply_count=float(reply_count_raw.strip('w'))*10000
            else:
                reply_count=int(reply_count_raw)

            return reply_count

        def deal_content_url(id_raw):
            return 'http://appapi.jiemian.com/v4/5.1.0/10001/article/'+str(id_raw)+'.json?code_p=51&code_c=51&vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI'

        def deal_publish_time(publishtimestamp):
            publish_time=time.localtime(int(publishtimestamp))
            return time.strftime('%Y-%m-%d %H:%M:%S',publish_time)


        board_response_json=json.loads(response.text)
        for one_article in board_response_json['result']['list']:
            metadata_in_for=copy.copy(metadata)


            try:
                article=one_article['article']
            except:
                continue
            _id= article['ar_id']  # id
            abstract=article['ar_sum']
            title =article['ar_tl']  # title
            reply_count= article['ar_cmt']  # 评论数
            read_count= article['ar_hit']  # 点击数
            url= article['ar_surl']  # url
            publish_user= article['ar_an']  # publish_user
            publicTimestamp=article['ar_pt']


            publish_time=deal_publish_time(publicTimestamp)
            reply_count=deal_reply_count(reply_count)
            one_news_dict={
                'id':str(_id),
                'title':str(title),
                'reply_count':reply_count,
                'read_count':read_count,
                'url':str(url),
                'publish_user':str(publish_user),
                'publish_time':publish_time,
                'publicTimestamp':int(str(publicTimestamp)),
                'abstract':str(abstract),
                'params':None,
                'appname': 'JieMianXinWen',
                'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            metadata_in_for.update(one_news_dict)
            content_url=deal_content_url(_id)



            yield scrapy.Request(url=content_url,headers=self.mobile_app_headers,meta={'pre_data':one_news_dict},callback=self.deal_content)





    def deal_content(self,response):
        metadata=response.meta['pre_data']


        def deal_content(datajson,content_dealed):
            #to save the probram that img don't show
            img_url_dict_all = {}
            for num, img_url_dict in enumerate(datajson['result']['photos']):
                img_url_dict_all.update(
                    {
                        '[img:' + str(num) + ']': '<img src="' + str(img_url_dict['image']) + '">' + str(
                            img_url_dict['intro'].encode('utf-8')) + '</img>'
                    }
                )

            def replace_img(match):
                return img_url_dict_all[match.group(0)]

            content = re.sub(r'\[img\:\d{1,2}\]', replace_img, content_dealed)
            return content

        def deal_comment_url(id_raw):
            return 'http://appapi.jiemian.com/v4/5.1.0/10001/comment/get_article_comment/'+id_raw+'.json?vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI'


        content_response_json=json.loads(response.text)
        try:
            author_list=content_response_json['result']['author_list'][0]
        except:
            return

        uid = author_list['uid']
        publish_user = author_list['name']
        publish_user_photo = author_list['head_img']
        content_raw = content_response_json['result']['article']['ar_con']
        content_dealed = unquote(content_raw)#将字符串转化为html的string内容。

        content=deal_content(content_response_json,content_dealed)
        comment_url=deal_comment_url(metadata['id'])

        content_dict={
            'publish_user_id':uid,
            'publish_user':publish_user,
            'publish_user_photo':publish_user_photo,
            'content':content,
            'reply_nodes':[]
        }
        metadata.update(content_dict)



        yield scrapy.Request(url=comment_url,headers=self.mobile_app_headers,meta={'pre_data':metadata},callback=self.deal_comments)





    def deal_comments(self,response):
        metadata=response.meta['pre_data']


        comment_response_json=json.loads(response.text)
        for one_comment in comment_response_json['result']['rst']:
            id = one_comment['id']
            content = one_comment['content']
            like_count = one_comment['praise']
            publish_time_stramp = str(one_comment['published'])
            publish_user_id = one_comment['user']['uid']
            publish_user = one_comment['user']['nike_name']
            publish_user_photo = one_comment['user']['head_img']
            publish_time_a = time.localtime(int(publish_time_stramp))
            publish_time = time.strftime('%Y-%m-%d %H:%M:%S', publish_time_a)

            comment_dict = {
                'id': id,
                'content': content,
                'like_count': like_count,
                # 'publish_time_stramp':publish_time_stramp,
                'publish_time': publish_time,
                'publish_user_id': publish_user_id,
                'publish_user': publish_user,
                'publish_user_photo': publish_user_photo,
                'parent_id': metadata['id'],
                'ancestor_id': metadata['id']
            }

            metadata['reply_nodes'].append(comment_dict)

        print('yield a data')
        yield standard(metadata)


        # if next_cmt_url:
        #     yield scrapy.FormRequest(url=next_cmt_url,headers=self.mobile_app_headers,formdata=formdata,meta={'pre_data':metadata,'formdata':formdata,},callback=self.deal_comments,dont_filter=True)
        # else:
        #     # print('has finished one----',metadata['url'])
        #     yield standard(metadata)
        #     # yield metadata