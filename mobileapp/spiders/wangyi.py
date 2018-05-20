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

        def get_request_for_debug():
            task_list=[
                {
                    'url':'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId':'T1457068979049',
                    'abstract':None,
                    'params':None,
                    'appname':'wangyi',
                    'channelName':'视频',
                    'request_data':{
                        'channel':'T1457068979049',
                        'subtab':'Video_Recom',
                        'size':'10',
                        'offset':'0',
                        'fn':'1',
                        'passport':'',
                        'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                        'lat':'',
                        'lon':'',
                        'version':'35.1',
                        'net':'wifi',
                        # 'ts':'1526776833',
                        # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                        # 'encryption':'1',
                        # 'canal':'news_lljc3',
                        'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                        'open':'',
                        'openpath':''
                    }
                },
                # {
                #     'url': 'http://c.m.163.com/recommend/getSubDocPic',
                #     'channelId': 'T1348647909107',
                #     'abstract': None,
                #     'params': None,
                #     'appname': 'wangyi',
                #     'channelName': '头条',
                #     'request_data':{
                #         'tid':'T1348647909107',
                #         'from':'toutiao',
                #         'offset':'20',
                #         'size':'10',
                #         'fn':'1',
                #         'LastStdTime':'1526756888',
                #         'spestr':'shortnews',
                #         'prog':'',
                #         # 'passport':'',
                #         'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                #         # 'lat':'',
                #         # 'lon':'',
                #         # 'version':'35.1',
                #         # 'net':'wifi',
                #         # 'ts':'1526773568',
                #         # 'sign':'Kr8H5/efevcqnpXLD6j4pyk/QKy7LsH5M0sslXNj5g148ErR02zJ6/KXOnxX046I',
                #         # 'encryption':'1',
                #         'canal':'news_lljc3',
                #         # 'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                #         # 'open':'',
                #         # 'openpath':''
                #     }
                # },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1467284926140',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '要闻',
                    'request_data':{
                            'from':'T1467284926140',
                            'size':'10',
                            'offset':'0',
                            'fn':'1',
                            'passport':'',
                            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                            'lat':'',
                            'lon':'',
                            'version':'35.1',
                            'net':'wifi',
                            # 'ts':'1526776833',
                            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                            # 'encryption':'1',
                            # 'canal':'news_lljc3',
                            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                            'open':'',
                            'openpath':''
                        }
                },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1348649580692',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '科技',
                    'request_data':{
                            'from':'T1348649580692',
                            'size':'10',
                            'offset':'0',
                            'fn':'1',
                            'passport':'',
                            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                            'lat':'',
                            'lon':'',
                            'version':'35.1',
                            'net':'wifi',
                            # 'ts':'1526776833',
                            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                            # 'encryption':'1',
                            # 'canal':'news_lljc3',
                            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                            'open':'',
                            'openpath':''
                        }
                },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1348648756099',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '财经',
                    'request_data':{
                            'from':'T1348648756099',
                            'size':'10',
                            'offset':'0',
                            'fn':'1',
                            'passport':'',
                            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                            'lat':'',
                            'lon':'',
                            'version':'35.1',
                            'net':'wifi',
                            # 'ts':'1526776833',
                            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                            # 'encryption':'1',
                            # 'canal':'news_lljc3',
                            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                            'open':'',
                            'openpath':''
                        }

                },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1348648141035',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '军事',
                    'request_data': {
                        'from': 'T1348648141035',
                        'size': '10',
                        'offset': '0',
                        'fn': '1',
                        'passport': '',
                        'devId': 'iBqHGWB8Yx8XkfAf9bTKRw==',
                        'lat': '',
                        'lon': '',
                        'version': '35.1',
                        'net': 'wifi',
                        # 'ts':'1526776833',
                        # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                        # 'encryption':'1',
                        # 'canal':'news_lljc3',
                        'mac': 'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                        'open': '',
                        'openpath': ''
                    }

                },

            ]
            for one_task in task_list:
                yield scrapy.FormRequest(method='GET',url=one_task['url'],headers=self.brownser_headers,meta={'pre_data':one_task},callback=self.deal_board_notoutiao,formdata=one_task['request_data'])
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
        #         'appname': one_board['appName'],
        #         'channelName': one_board['channelName']
        #     }
        #     yield scrapy.Request(url=one_board_info['url'],headers=self.brownser_headers,meta={'pre_data':one_board_info},callback=self.deal_board)
        # client.close()

    def deal_board_notoutiao(self,response):
        '''
        :param response:
        :return: return the request for some content sepecificly
        :notice: the different board may have differnet Json structure
        :notice: video's url is deferent from others.the video's url is http://m.thepaper.cn/channel_26916;
        :notice:

        '''

        metadata=response.meta['pre_data']

        def deal_content_url(data):
            id=data['id']
            return 'https://c.m.163.com/nc/article/'+str(id)+'/full.html'

        datajson=json.loads(response.text)

        if '推荐' in datajson.keys():
            all_article=datajson['推荐']
            for one_article in all_article:
                metadata_in_for=copy.copy(metadata)
                title=one_article['title']
                source=one_article['source']
                publish_time=one_article['ptime']
                reply_count=one_article['replyCount']
                _id=one_article['id']
                abstract=one_article['digest']

                one_article_dict={
                    'title':title,
                    'source':source,
                    'publish_time':publish_time,
                    'reply_count':reply_count,
                    'id':_id,
                    'abstract':abstract
                }

                metadata_in_for.update(one_article_dict)

                url=deal_content_url(metadata_in_for)
                metadata_in_for['url']=url
                headers={
                        'Accept-Encoding':'gzip',
                        'Connection':'Keep-Alive',
                        'Host':'c.m.163.com',
                        'X-NR-Trace-Id':'1526809832821_50263131_863213510134567',
                        'User-Agent':'NewsApp/35.1 Android/5.1.1 (samsung/SM-G9350)',
                        'User-C':'5aix5LmQ',
                    }

                yield scrapy.Request(url=url,meta={'pre_data':metadata_in_for},headers=headers,callback=self.deal_content)






        # data_re_url=response.selector.re('data	:	\"(.*?)\".*?Math\.random')
        #
        #
        #
        #
        # if data_re_url:
        #     if 'http://m.thepaper.cn/channel_26916' in response.url:
        #         next_url_for_content='http://www.thepaper.cn/load_index.jsp?' + data_re_url[0]
        #         next_callback=self.deal_board_Movie
        #     else:
        #         next_url_for_content = 'http://m.thepaper.cn/load_channel.jsp?' + data_re_url[0]
        #         next_callback=self.deal_board_Article
        #
        #     metadata=response.meta['pre_data']
        #
        #
        #     yield scrapy.Request(url=next_url_for_content,headers=self.brownser_headers,meta={'pre_data':metadata},callback=self.deal_content)

    def deal_content(self,response):
        metadata=response.meta['pre_data']
        metadata['reply_nodes']=[]
        _id=metadata['id']


        def deal_comments_urls():
            post_data = {
                    'offset':'0',
                    'limit':'20',
                    'showLevelThreshold':'5',
                    'headLimit':'3',
                    'tailLimit':'2',
                    }
            return post_data

        datajson=json.loads(response.text)
        if _id in datajson.keys():
            content_data=datajson[_id]
            content=content_data['body']
            like_count=content_data['threadVote']
            reply_count=content_data['replyCount']

            article_content_dict={
                'content':content,
                'like_count':like_count,
                'reply_count':reply_count
            }
            metadata.update(article_content_dict)


            cmt_params=deal_comments_urls()
            cmt_urls='https://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/DI8G906G0001875P/app/comments/newList'
            headers={
                'Accept-Encoding':'gzip',
                'Connection':'Keep-Alive',
                'Host':'comment.api.163.com',
                'X-NR-Trace-Id':'1526813455392_951419013_863213510134567',
                'User-Agent':'NewsApp/35.1 Android/5.1.1 (samsung/SM-G9350)',
                'User-C':'6KaB6Ze7',
                'User-N':'wKq3+ZhKJshqLUdmuO/3GU54yPhI0ZGYXNBL+qbp+gYtkyOvjJ64oHfDp3tOH9cB'
            }
            yield scrapy.FormRequest(url=cmt_urls,method='GET',formdata=cmt_params,meta={'pre_data':metadata},headers=headers,callback=self.deal_comments)







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

        for one_cmt_key in datajson['comments'].keys():
            publish_user_id=one_cmt_key

            one_cmt=datajson['comments'][one_cmt_key]
            id = one_cmt['postId']
            content = one_cmt['content']
            publish_user_id = one_cmt['userId']
            dislike_count=one_cmt['against']
            publish_time=one_cmt['createTime']
            like_count=one_cmt['favCount']
            ip=one_cmt['ip']
            sharecount=one_cmt['shareCount']

            try:
                publish_user=one_cmt['user']['nickname']
            except:
                publish_user='有态度的网友'
                continue
            try:
                publish_user_id=one_cmt['user']['userId']
            except:
                publish_user_id=''
            try:
                address=one_cmt['user']['location']
            except:
                address=''
            try:
                publish_user_photo=one_cmt['avatar']
            except:
                publish_user_photo=''



