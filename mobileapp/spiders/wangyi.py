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





class wangyi(Spider):
    name = 'wangyi'



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

        mongocfg=DOC.find({'appName':'thepaper','recommend':{'$gt':0}})
        for one_board in mongocfg:
            one_board_info = {
                'url': one_board['url'],
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
        :return: request to be deal ,for getting board info;
        :notice: the url next to visit for get content is like this:--http://www.thepaper.cn/load_index.jsp?nodeids=26912,26918,26965,26908,27260,26907,26911,26913,26906,26909,26910,26914,26915,26919,&topCids=2051901,2054797,2052136&pageidx=
                 the "nodeids=26912,26918,26965,26908,27260,26907,26911,26913,26906,26909,26910,26914,26915,26919,&topCids=2051901,2054797,2052136&pageidx=" come from
                 this board index page,and find by /*re('data	:	\"(.*?)\".*?Math\.random\b')*/;
        :notice: video's url is deferent from others.the video's url is http://m.thepaper.cn/channel_26916;
        :notice:

        '''

        data_re_url=response.selector.re('data	:	\"(.*?)\".*?Math\.random')
        if data_re_url:
            if 'http://m.thepaper.cn/channel_26916' in response.url:
                next_url_for_content='http://www.thepaper.cn/load_index.jsp?' + data_re_url[0]
                next_callback=self.deal_board_Movie
            else:
                next_url_for_content = 'http://m.thepaper.cn/load_channel.jsp?' + data_re_url[0]
                next_callback=self.deal_board_Article

            metadata=response.meta['pre_data']


            yield scrapy.Request(url=next_url_for_content,headers=self.brownser_headers,meta={'pre_data':metadata},callback=next_callback)

    def deal_content(self,response):
        metadata=response.meta['pre_data']
        metadata['reply_nodes']=[]

        def deal_publish_time(publish_time):
            if publish_time:
                return str(publish_time[0])+':00'
            else:
                return '1111-11-11 11:11:11'

        def deal_comments_urls(comment_data):
            post_data = {
                'WD-UUID': '861557177515977',
                'WD-CLIENT-TYPE': '04',
                'WD-UA': 'oneplus_a3010_android',
                'WD-VERSION': '4.4.6',
                'WD-CHANNEL': '360sjzs',
                'WD-RESOLUTION': '720*1256',
                'userId': '2704158',
                'WD-TOKEN': 'd2d2344c928de46787d06b6574c9fea0',
            }
            post_data['c']=comment_data['id']
            return post_data

        def deal_like_count(like_count_raw):
            return int(like_count_raw[0]) if like_count_raw else 0



        content=response.xpath('//div[@class="news_content"]/div[@class="news_part_father"]').extract_first()
        publish_time_raw=response.xpath('//div[@class="news_content"]//p[@class="about_news"]/text()').re('(\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}\:\d{1,2})')
        publish_user=response.xpath('//div[@class="news_content"]//p[@class="about_news" and not(@style)]/text()').extract_first(default='')
        img_urls=response.xpath('//div[@class="news_content"]//img/@src').extract()
        video_urls=response.xpath('//div[@class="news_content"]//source/@src').extract()
        like_count_raw = response.xpath('//a[@id="news_praise"]/text()').re('\d+')


        publish_time=deal_publish_time(publish_time_raw)
        like_count=deal_like_count(like_count_raw)


        article_data={
            'content':content,
            'publish_time':publish_time,
            'publish_user':publish_user,
            'img_urls':img_urls,
            'video_urls':video_urls,
            'like_count':like_count
        }
        # article_data.update
        metadata.update(article_data)
        url_cmt = 'http://app.thepaper.cn/clt/jsp/v3/contFloorCommentList.jsp'
        formdata=deal_comments_urls(metadata)

        return scrapy.FormRequest(url=url_cmt,headers=self.mobile_app_headers,meta={'pre_data':metadata,'formdata':formdata},formdata=formdata,callback=self.deal_comments)

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