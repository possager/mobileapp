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





class thepaper(Spider):
    name = 'thepaper'



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
            yield scrapy.Request(url=one_board_info['url'],headers=self.brownser_headers,meta={'pre_data':one_board_info},callback=self.deal_board_next)
        client.close()



    def deal_board_next(self,response):
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

    def deal_board_Article(self,response):
        metadata=response.meta['pre_data']

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
        def deal_id(id):
            if id:
                return id.split('_')[-1]
        def deal_url(id):
            return 'http://m.thepaper.cn/'+id

        for one_article in response.xpath('.//div[@class="t_news"]'):
            metadata_in_for=copy.copy(metadata)
            title=one_article.xpath('.//div[@class="txt_t"]/div[@class="news_tit02"]/p/a/text()').extract_first(default='')
            article_id_raw=one_article.xpath('.//div[@class="txt_t"]/div[@class="news_tit02"]/p/a/@href').extract_first(default=None)
            publish_time_raw=one_article.xpath('.//div[@class="txt_t"]//p[@class="news_info"]/span[@class="news_time bgimg_time"]/text()').extract_first(default='')
            source=one_article.xpath('.//div[@class="txt_t"]//p[@class="news_info"]/a/text()').extract()
            reply_count=one_article.xpath('.//div[@class="txt_t"]//p[@class="news_info"]/span[@class="news_time bgimg_comm"]/text()').extract_first(default=0)


            publish_time_dealed=deal_publish_time(publish_time_raw)
            id=deal_id(article_id_raw)
            url=deal_url(article_id_raw)


            data_in_board={
                'title':title,
                'id':id,
                'url':url,
                'source':source,
                'reply_count':reply_count,
                'publish_time':publish_time_dealed
            }
            # data_in_board.update(metadata)
            metadata_in_for.update(data_in_board)

            yield scrapy.Request(url=url,headers=self.brownser_headers,meta={'pre_data':metadata_in_for},callback=self.deal_content_Article)

    def deal_board_Movie(self,response):
        metadata=response.meta['pre_data']


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

        def deal_url(url_raw):
            return 'http://m.thepaper.cn/'+url_raw

        def deal_id(url_raw):
            return url_raw.split('_')[-1]


        marknum=1

        request_list=[]
        for one_article in response.xpath('//div[@class="news_li"]'):
            metadata_in_for=copy.copy(metadata)
            title = one_article.xpath('.//h2/a[@id]/text()').extract_first(
                default='')
            url_raw=one_article.xpath('.//h2/a/@href').extract_first(default=None)
            publish_time_raw = one_article.xpath(
                './/div[@class="pdtt_trbs"]/span[not(@class)]/text()').extract_first(
                default='')
            reply_count = one_article.xpath(
                './/div[@class="pdtt_trbs"]/span[@class="trbszan"]/text()').extract_first(
                default=0)


            publish_time=deal_publish_time(publish_time_raw)
            url=deal_url(url_raw)

            data_in_board={
                'title':title,
                'id':deal_id(url_raw),
                'url':copy.copy(url),
                'publish_time':publish_time,
                'reply_count':reply_count
            }
            # data_in_board.update(metadata)
            metadata_in_for.update(data_in_board)
            request1= scrapy.Request(url=copy.copy(url), headers=self.brownser_headers,
                                      meta={'pre_data': metadata_in_for,'mark_num':marknum},
                                      callback=self.deal_content_Movie)
            print(url)
            print(metadata_in_for)

            request_list.append(request1)
            marknum+=1

        for x,one_request in enumerate(request_list):
            yield one_request




    def deal_content_Article(self,response):
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

    def deal_content_Movie(self,response):
        metadata=response.meta['pre_data']


        def deal_like_count(like_count_raw):
            return int(like_count_raw[0]) if like_count_raw else 0

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

        def deal_publish_time(publish_time_raw):
            if type(publish_time_raw) ==type([]):
                return str(publish_time_raw[0])+':00'#经过re正则匹配到的，字符串的前半部分一定是满足条件的
            elif type(publish_time_raw)==type(''):
                return str(publish_time_raw)+':00'
            else:
                return publish_time_raw

        def deal_img_urls(img_urls_raw):
            img_urls =[]
            for one_img_url in img_urls_raw:
                if 'http' not in one_img_url:
                    img_urls.append('http:'+one_img_url)
                else:
                    img_urls.append(one_img_url)


        content=response.xpath('//div[@class="news_content"]').extract_first(default='')
        publish_time=response.xpath('//div[@class="news_video_name"]').re('\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}')
        img_urls=response.xpath('//div[@class="news_content"]//img/@src').extract()
        video_urls=response.xpath('//video/source/@src').extract()
        like_count_raw=response.xpath('//a[@id="news_praise"]/text()').re('\d+')


        like_count=deal_like_count(like_count_raw)
        publish_time=deal_publish_time(publish_time)
        img_urls=deal_img_urls(img_urls)


        movie_data={
            'content':content,
            'publish_time':publish_time,
            'img_urls':img_urls,
            'video_urls':video_urls,
            'like_count':like_count,
            'reply_nodes':[]
        }
        # movie_data.update(metadata)
        metadata.update(movie_data)

        url_cmt = 'http://app.thepaper.cn/clt/jsp/v3/contFloorCommentList.jsp'
        formdata = deal_comments_urls(metadata)


        # print('has yield one requests to deal_comment',metadata['url'])
        return scrapy.FormRequest(url=url_cmt,headers=self.mobile_app_headers,formdata=formdata,meta={'pre_data':metadata,'formdata':formdata,},callback=self.deal_comments)



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