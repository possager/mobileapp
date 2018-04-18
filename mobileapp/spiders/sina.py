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





class sina(Spider):
    name = 'sina'



    brownser_headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
    }
    mobile_app_headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
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

        def deal_board_url(news_id):
            return 'https://cre.dp.sina.cn/api/v3/get?&cre=tianyi&mod='+str(news_id)+'&local_code=sc'



        client=pymongo.MongoClient('178.16.7.86',27017)
        COL=client['news']
        DOC=COL['channellist']

        mongocfg=DOC.find({'appName':'sina','recommend':{'$gt':0}})
        for one_board in mongocfg:
            one_board_info = {
                'url': deal_board_url(one_board['channelId']),
                'channelId': one_board['channelId'],
                'abstract': None,
                'params': None,
                'appname': one_board['appName'],
                'channelName': one_board['channelName']
            }
            yield scrapy.Request(url=one_board_info['url'],headers=self.brownser_headers,meta={'pre_data':one_board_info},callback=self.deal_board)
        client.close()



    def deal_board(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publicTimestamp_raw):
            timetuple=time.localtime(int(publicTimestamp_raw))
            publish_time=time.strftime('%Y-%m-%d %H:%M:%S',timetuple)
            return publish_time

        datajson=json.loads(response.text)

        for one_aritcle in datajson['data']:
            metadata_in_for=copy.copy(metadata)

            source=one_aritcle['media'] if 'media' in one_aritcle.keys() else None
            title=one_aritcle['title'] if 'title' in one_aritcle.keys() else None
            publicTimestamp=one_aritcle['ctime'] if 'ctime' in one_aritcle.keys() else None
            url=one_aritcle['url'] if 'url' in one_aritcle.keys() else None
            abstract=one_aritcle['short_intro'] if 'short_intro' in one_aritcle.keys() else None
            publish_user_id=one_aritcle['authorId'] if 'authorId' in one_aritcle.keys() else None
            _id = one_aritcle['_id'] if '_id' in one_aritcle.keys() else None
            comment_id=one_aritcle['commentid'] if 'commentid' in one_aritcle.keys() else None
            original_reply_count=one_aritcle['comment_count'] if 'comment_count' in one_aritcle.keys() else 0
            publish_user= one_aritcle['author'] if 'author' in one_aritcle.keys() else None
            keywords=one_aritcle['labels_show'] if 'labels_show' in one_aritcle.keys() else None
            reply_count=one_aritcle['comment_count_show'] if 'comment_count_show' in one_aritcle.keys() else 0


            one_article_dict={
                'source':source,
                'title':title,
                'publicTimestamp':publicTimestamp,
                'url':url,
                'abstract':abstract,
                'publish_user_id':publish_user_id,
                'id':_id,
                'comment_id':comment_id,
                'publish_user':publish_user,
                'params':{
                    'original_reply_count':original_reply_count,
                    'keywords':keywords
                },
                'publish_time':deal_publish_time(publicTimestamp),
                'reply_count':reply_count
            }
            metadata_in_for.update(one_article_dict)
            if one_article_dict['url'] and one_article_dict['id']:
                yield scrapy.Request(url=one_article_dict['url'],headers=self.brownser_headers,meta={'pre_data':one_article_dict},callback=self.deal_content)




    def deal_content(self,response):
        metadata=response.meta['pre_data']
        metadata['reply_nodes']=[]


        content=response.xpath('//article[@class="art_box"]').extract_first()
        img_urls=response.xpath('//article[@class="art_box"]//img/@src').extract()

        if not content:
            content=response.xpath('//section[@class="card_module"]').extract_first()
            img_urls=response.xpath('//section[@class="card_module"]//img/@src').extract_first()


        content_dict={
            'content':content,
            'img_urls':img_urls
        }

        metadata.update(content_dict)




        # return scrapy.FormRequest(url=url_cmt,headers=self.mobile_app_headers,meta={'pre_data':metadata,'formdata':formdata},formdata=formdata,callback=self.deal_comments)



    def deal_comments(self,response):
        metadata=response.meta['pre_data']
        formdata=response.meta['formdata']

        def deal_publish_time(publish_time_raw):
            '''
            :param publish_time_raw:
            :return:
            :notice:这里的publish_time后边反正也会更新
            '''
            if publish_time_raw:
                if '分钟前' in publish_time_raw:
                    minulate = publish_time_raw.replace('分钟前', '')
                    time_b = datetime.datetime.now() - timedelta(minutes=int(minulate))
                    publish_time = time_b.strftime('%Y-%m-%d %H:%M:%S')
                elif '小时前' in publish_time_raw:
                    hours = publish_time_raw.replace('小时前', '')
                    time_b = datetime.datetime.now() - timedelta(hours=int(hours))
                    publish_time = time_b.strftime('%Y-%m-%d %H:%M:%S')
                elif '天前' in publish_time_raw:
                    days = publish_time_raw.replace('天前', '')
                    time_b = datetime.datetime.now() - timedelta(days=int(days))
                    publish_time = time_b.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    return '1111-11-11 11:11:11'
                return publish_time
        def deal_parent_id(parent_id,ancestor_id):
            if parent_id==0:
                return ancestor_id
            else:
                return parent_id

        datajson = json.loads(response.text)
        next_cmt_url=datajson['nextUrl']

        for one_cmt in datajson['commentList']:
            id = one_cmt['commentId']
            content = one_cmt['content']
            publish_user_id = one_cmt['userId']
            publish_user = one_cmt['userName']
            like_count = one_cmt['praiseTimes']  # like_count
            publish_time_raw = one_cmt['pubTime']  # publish_time
            publish_user_photo = one_cmt['userInfo']['pic']
            ancestor_id = one_cmt['contId']  #
            parent_id = one_cmt['parentId']




            publish_time=deal_publish_time(publish_time_raw)
            parent_id=deal_parent_id(parent_id,ancestor_id)

            one_cmt_dict = {
                'id': id,
                'content': content,
                'publish_usr_id': publish_user_id,
                'publish_user': publish_user,
                'like_count': like_count,
                'publish_time': publish_time,
                'publish_user_photo': publish_user_photo,
                'ancestor_id': ancestor_id,
                'parent_id': parent_id
            }
            metadata['reply_nodes'].append(one_cmt_dict)


        if next_cmt_url:
            return scrapy.FormRequest(url=next_cmt_url,headers=self.mobile_app_headers,formdata=formdata,meta={'pre_data':metadata,'formdata':formdata,},callback=self.deal_comments,dont_filter=True)
        else:
            # print('has finished one----',metadata['url'])
            return standard(metadata)
            # yield metadata