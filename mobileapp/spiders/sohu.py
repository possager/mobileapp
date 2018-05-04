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
import urllib.parse





class sohu(Spider):
    name = 'sohu'



    brownser_headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'Connection':'keep-alive',
        'Cache-Control':'max-age=0',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Accept-Encoding':'gzip, deflate'
    }
    mobile_app_headers={
        'STM': '1525399145234',
        'SNONCE': "1977539389",
        'SCOOKIEV2': '7XmaWntDsPhAEdmVUN/Ip6+wbE31Gd8vRZ5/R6VJbbq2WCGhAW8Ppcmps+K7jvOi0uW7tgusa6QiP6y5VnVOu99Ne9fzzc+Uwir/6UmQ97ajRMo2ePyKLgDJJsAaYDyWqlJL85AjvRb3260UiuqOR2vX48gXmZFUMwymhOnxGoA8992IttsmC+MuyXzrPlu7g/VoTJRn4uXCxoxPI8hkBdWBoad0jZpI1OguKsDsw/Jjxs1usyVyX22iry4ljNMH7aPaSVUHdhsth/sYAS9qTqfjmFkZ2iRjgnWYjH6p9KKKGkU/oSrv5hnp5bZbvx7UK6JAXEPWz+6GgW7borhi+icPnQ2Atj7OsZWxN4qm3EW1e+1+OUhhHG1SKGeIL2sf',
        'REQID': '4b465683e2434666bbb71a62f8cc484d',
        'SSIG': '85e96ccdd1ece817a737017a19c136b0',
        'SVER': '1517381440|',
        'Host': 'api.k.sohu.com',
        'Connection': 'close',
        'User-Agent': 'okhttp/3.9.1'
    }


    def start_requests(self):

        def get_request_for_debug():
            task_list=[
                {
                    'url':'https://api.k.sohu.com/api/channel/v6/news.go',
                    'channelId':'1',
                    'abstract':None,
                    'params':None,
                    'appname':'sohu',
                    'channelName':'要闻'
                },
                # {
                #     'url': 'https://api.k.sohu.com/api/channel/v6/news.go',
                #     'channelId': '13557',
                #     'abstract': None,
                #     'params': None,
                #     'appname': 'sohu',
                #     'channelName': '推荐'
                # },
                {
                    'url': 'https://api.k.sohu.com/api/channel/v6/news.go',
                    'channelId': '283',
                    'abstract': None,
                    'params': None,
                    'appname': 'sohu',
                    'channelName': '成都'
                },
                {
                    'url': 'https://api.k.sohu.com/api/channel/v6/news.go',
                    'channelId': '3',
                    'abstract': None,
                    'params': None,
                    'appname': 'sohu',
                    'channelName': '娱乐'
                },
                {
                    'url': 'https://api.k.sohu.com/api/channel/v6/news.go',
                    'channelId': '247',
                    'abstract': None,
                    'params': None,
                    'appname': 'sohu',
                    'channelName': '生活'
                },

            ]

            formdata_for_board_requests={
                'p1':'NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D',
                'pid':'-1',
                'channelId':'1',
                'num':'20',
                'imgTag':'1',
                'showPic':'1',
                'picScale':'11',
                'rt':'json',
                'net':'wifi',
                'from':'channel',
                'v':'1525363200',
                'forceRefresh':'1',
                'times':'0',
                'page':'1',
                'action':'0',
                'mode':'0',
                'cursor':'0',
                'mainFocalId':'0',
                'focusPosition':'1',
                'viceFocalId':'0',
                'lastUpdateTime':'0',
                'u':'1',
                'source':'0',
                'actiontype':'1',


            }

            for one_task in task_list:
                formdata_for_board_requests['channelId']=one_task['channelId']
                yield scrapy.FormRequest(method='GET',url=one_task['url'],headers=self.mobile_app_headers,meta={'pre_data':one_task},callback=self.deal_board,formdata=formdata_for_board_requests)
        for i in get_request_for_debug():
            yield i

        # client=pymongo.MongoClient('178.16.7.86',27017)
        # COL=client['news']
        # DOC=COL['channellist']
        #
        # mongocfg=DOC.find({'appName':'changdu','recommend':{'$gt':0}})
        # for one_board in mongocfg:
        #     one_board_info = {
        #         'url': 'http://interfacev5.vivame.cn/x1-interface-v5/json/newdatalist.json',
        #         'channelId': one_board['channelId'],
        #         'abstract': None,
        #         'params': None,
        #         'appname': one_board['appName'],
        #         'channelName': one_board['channelName']
        #     }
        #     post_data={
        #         "platform": "android",
        #          "installversion": "6.7.0.1",
        #          "channelno": "MZSDA2320480100",
        #          "mid": "cb8de243d6ca911fc673ab4bab1dfecd",
        #          "uid": "14400699",
        #          "sid": "75ip2pfj-32j8-nebk-kec5-ed61b7956312",
        #          "type":"1",
        #          "category": "1",
        #          "ot": "0",
        #          "nt": "0",
        #         'id':one_board_info['channelId']
        #     }
        #
        #     yield scrapy.FormRequest(url=one_board_info['url'],headers=self.mobile_app_headers,meta={'pre_data':one_board_info},formdata=post_data,callback=self.deal_board)
        # client.close()



    def deal_board(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publicTimestamp):
            time_tuple=time.localtime(int(publicTimestamp/1000))
            publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
            return publish_time


        datajson=json.loads(response.text)
        for one_article in datajson['recommendArticles']:
            if one_article['editNews']:#有广告，广告该字段为false

                metadata_in_for=copy.copy(metadata)



                _id=one_article['newsId']
                publicTimestamp=int(one_article['time']/1000)
                title=one_article['title']
                source=one_article['media']




                publish_time=deal_publish_time(publicTimestamp)

                one_article_dict={
                    'id':str(_id),
                    'title':title,
                    'publicTimestamp':publicTimestamp,
                    'publish_time':publish_time,
                    'source':source
                }
                metadata_in_for.update(one_article_dict)

                yield scrapy.Request(url=url,meta={'pre_data':metadata_in_for},headers=self.brownser_headers,callback=self.deal_content)








    def deal_content(self,response):
        metadata=response.meta['pre_data']
        metadata['reply_nodes']=[]


        def deal_comment_urls(news_id):
            # comment_url="http://interfacev5.vivame.cn/x1-interface-v5/json/commentlist.json?platform=android&installversion=6.2.2.2&channelno=AZWMA2320480100&mid=5284047f4ffb4e04824a2fd1d1f0cd62&uid=3125&sid=f4umcvbs-4154-495a-b13f-2245a758834a&type=0&id=" + str(news_id) + "&pageindex=0&pagesize=20&commentType=4"
            comment_url2='https://interfacev5.vivame.net.cn/x1-interface-v5/json/commentlist.json?uid=15155081&platform=android&installversion=7.0.6&channelno=VIVAA2320480100&sid=&latlng=31.247631,121.497856&id='+str(news_id)+'&type=&pageindex=1&pagesize=10&commentType=4&appId=83ee783f8111b5ec3f0d888d0e5a0381&tk=01iofi8o-64oe-j61l-i389-3e66bc946ff9&_='+str(time.time()*1000)

            return comment_url2


        content=response.xpath('//div[@id="aMain"]/div[@class="text"]').extract()
        img_urls=response.xpath('//div[@id="aMain"]/div[@class="text"]//img/@data-src').extract()


        content_dict={
            'content':content,
            'img_urls':img_urls
        }

        metadata.update(content_dict)

        comment_urls=deal_comment_urls(metadata['id'])
        yield scrapy.Request(url=comment_urls,headers=self.mobile_app_headers,meta={'pre_data':metadata},callback=self.deal_comments)




    def deal_comments(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publish_time_stamp):
            time_tuple=time.localtime(publish_time_stamp)
            publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
            return publish_time

        def deal_comment_url_next(cmt_url):
            cmt_url_splited=cmt_url.split('&pageindex=')
            page_STR_int=cmt_url_splited[1].split('&')[0]
            cmt_url_next=cmt_url_splited[0]+'&pageindex='+str(int(page_STR_int)+1)+'&pagesize=10&commentType=4&appId=83ee783f8111b5ec3f0d888d0e5a0381&tk=01iofi8o-64oe-j61l-i389-3e66bc946ff9&_='+str(time.time()*1000)

            return cmt_url_next
        datajson=json.loads(response.text)
        for one_cmt in datajson['data']:
            _id=one_cmt['id']
            publicTimestamp=int(one_cmt['createdAt']/1000)
            content=one_cmt['content']
            publish_user=one_cmt['communityUser']['nickName']
            publish_user_id=one_cmt['communityUser']['uid']
            publish_user_photo=one_cmt['communityUser']['headIcon']
            like_count=one_cmt['likeInfo']['likeCount']



            publish_time=deal_publish_time(publicTimestamp)

            one_comment_dict={
                'id':_id,
                'publicTimestamp':publicTimestamp,
                'content':content,
                'publish_user':publish_user,
                'publish_user_id':publish_user_id,
                'publish_user_photo':publish_user_photo,
                'like_count':like_count,
                'publish_time':publish_time,
                'parent_id':metadata['id'],
                'ancestor_id':metadata['id']
            }

            metadata['reply_nodes'].append(one_comment_dict)


        if len(datajson['data'])==10:
            return scrapy.Request(url=deal_comment_url_next(response.url),headers=self.mobile_app_headers,meta={'pre_data':metadata},callback=self.deal_comments)
        return standard(metadata)