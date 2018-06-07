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
            time_tuple=time.localtime(int(publicTimestamp))
            publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
            return publish_time

        def deal_params_for_content(data):
            content_params = {
                'channelId': '1',
                'apiVersion': '41',
                'gid': '-1',
                'imgTag': '1',
                'newsId': '274508914',
                'openType': '',
                'u': '1',
                'p1': 'NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D',
                'pid': '-1',
                'recommendNum': '3',
                'refer': '130',
                'rt': 'json',
                'showSdkAd': '1',
                'moreCount': '8',
                'articleDebug': '0',
            }
            content_params['newsId']=data['id']
            content_params['channelId']=data['channelId']

            return content_params



        datajson=json.loads(response.text)
        if 'recommendArticles' in datajson.keys():
            allarticle =datajson['recommendArticles']
        elif 'articles' in datajson.keys():
            allarticle=datajson['articles']
        else:
            return
        for one_article in allarticle:
            if one_article['editNews']:#有广告，广告该字段为false

                metadata_in_for=copy.copy(metadata)



                _id=one_article['newsId']
                publicTimestamp=int(int(one_article['time'])/1000)
                title=one_article['title']
                try:
                    source=one_article['media']
                except Exception as e:
                    source=''




                publish_time=deal_publish_time(publicTimestamp)

                one_article_dict={
                    'id':str(_id),
                    'title':title,
                    'publicTimestamp':publicTimestamp,
                    'publish_time':publish_time,
                    'source':source,
                    'url':'https://3g.k.sohu.com/t/n'+str(_id)
                }
                metadata_in_for.update(one_article_dict)

                content_parms=deal_params_for_content(metadata_in_for)
                article_url='https://api.k.sohu.com/api/news/v5/article.go'

                headers_content={
                        'Host':'api.k.sohu.com',
                        'Connection':'close',
                        'Accept':'*/*',
                        'X-Requested-With':'XMLHttpRequest',
                        'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350 Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36 JsKit/1.0 (Android);',
                        'Referer':'https://api.k.sohu.com/h5apps/newssdk.sohu.com/modules/article/article.html?newsId=274508914&from=channel&channelId=1&token=1527148981565&tracker=type:recom,engine:getui_1.0_v4&position=7&page=1&CDN_URL=https%3A%2F%2Fzcache.k.sohu.com%2Fapi%2Fnews%2Fcdn%2Fv5%2Farticle.go%2F274508914%2F0%2F0%2F0%2F3%2F1%2F12%2F41%2F3%2F1%2F1%2F1527068817021.json&isHasSponsorships=1&templateType=1&newsType=3&updateTime=1527068817021&isRecom=1',
                        'Accept-Language':'zh-CN,en-US;q=0.8',
                    }

                yield scrapy.FormRequest(method='GET',url=article_url,meta={'pre_data':metadata_in_for},headers=headers_content,formdata=content_parms,callback=self.deal_content)


    def deal_content(self,response):
        metadata=response.meta['pre_data']
        metadata['reply_nodes']=[]


        def deal_comment_request_params(news_id):
            # # comment_url="http://interfacev5.vivame.cn/x1-interface-v5/json/commentlist.json?platform=android&installversion=6.2.2.2&channelno=AZWMA2320480100&mid=5284047f4ffb4e04824a2fd1d1f0cd62&uid=3125&sid=f4umcvbs-4154-495a-b13f-2245a758834a&type=0&id=" + str(news_id) + "&pageindex=0&pagesize=20&commentType=4"
            # comment_url2='https://interfacev5.vivame.net.cn/x1-interface-v5/json/commentlist.json?uid=15155081&platform=android&installversion=7.0.6&channelno=VIVAA2320480100&sid=&latlng=31.247631,121.497856&id='+str(news_id)+'&type=&pageindex=1&pagesize=10&commentType=4&appId=83ee783f8111b5ec3f0d888d0e5a0381&tk=01iofi8o-64oe-j61l-i389-3e66bc946ff9&_='+str(time.time()*1000)
            request_dict={
                'busiCode':'2',
                'apiVersion':'41',
                'channelId':'1',
                'cursorId':'',
                # 'from':'1527217578021',
                # 'gid':'x011060802ff0dc5132b6d42f00069cd1e654860b7f5',
                'id':str(news_id),
                'openType':'',
                # 'p1':'NjM5Nzk4NjA1NTAzNTIwMzYxMQ%3D%3D',
                'u':'1',
                'page':'1',
                'pid':'-1',
                'position':'4',
                'refer':'3',
                'rollType':'1',
                'rt':'json',
                'size':'10',
                'source':'news',
                'subId':'130152',
                'type':'5',
                'refererType':'',
                'articleDebug':'',

            }
            return request_dict

        def deal_img_urls(picture_list):
            img_urls2=[]

            for one_img in picture_list:
                try:
                    img_urls2.append(one_img['pic'])
                except:
                    pass
            return img_urls2

        def deal_content(content,img_urls):
            img_repl_dict = {}
            for i in range(len(img_urls)):
                imgsub_dict = {
                    '<image_' + str(i) + '></image_' + str(i) + '>': '<img src="' + img_urls[i] + '"></img>'
                }
                img_repl_dict.update(imgsub_dict)

            def replaceimg(img_url):
                print(img_url)
                img_urls = img_url.group(0)
                return img_repl_dict[img_urls]

            content2 = re.sub('\<image\_\d*\>\<\/image\_\d*\>', replaceimg, content)
            return content2

        datajson=json.loads(response.text)

        try:
            content_raw=datajson['content']
            img_urls=deal_img_urls(datajson['photos'])
            content=deal_content(content_raw,img_urls)
        except:
            content=None
            img_urls=[]


        content_dict={
            'content':content,
            'img_urls':img_urls,
            'reply_nodes':[]
        }

        metadata.update(content_dict)

        comment_parms=deal_comment_request_params(metadata['id'])
        comment_urls='https://api.k.sohu.com/api/comment/getCommentListByCursor.go'
        headers={
    'Connection':'close',
    'Accept':'*/*',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350 Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36 JsKit/1.0 (Android);',
}
        yield scrapy.FormRequest(method='GET',url=comment_urls,headers=headers,meta={'pre_data':metadata,'formdata':comment_parms},callback=self.deal_comments,formdata=comment_parms)




    def deal_comments(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publish_time_stamp):
            time_tuple=time.localtime(publish_time_stamp)
            publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
            return publish_time

        def deal_comment_params_next(comment_data):
            page=comment_data['page']
            pageNext=str(int(page)+1)
            comment_data['page']=pageNext

            return comment_data

        datajson=json.loads(response.text)
        if 'response' in datajson.keys():
            if 'commentList' in datajson['response'].keys():
                for one_cmt in  datajson['response']['commentList']:
                    publish_user=one_cmt['author']
                    address=one_cmt['city']
                    _id=one_cmt['commentId']
                    content=one_cmt['content']
                    publicTimestamp=one_cmt['ctime']
                    like_count=one_cmt['digNum']
                    passport=one_cmt['passport']
                    reply_count=one_cmt['replyCount']

                    publish_time=deal_publish_time(int(int(publicTimestamp)/1000))

                    cmtDict={
                        'id':_id,
                        'publish_user':publish_user,
                        'content':content,
                        'publicTimestamp':publicTimestamp,
                        'like_count':like_count,
                        'publish_time':publish_time,
                        'reply_count':reply_count,
                        'params':{
                            'address':address,
                            'passport':passport,
                        }
                    }

                    metadata['reply_nodes'].append(cmtDict)
            else:
                return standard(metadata)
        else:
            return standard(metadata)

        if len(datajson['response']['commentList'])==10:
            comment_next_params=deal_comment_params_next(response.meta['formdata'])
            url_comment='https://api.k.sohu.com/api/comment/getCommentListByCursor.go'
            headers={
                'Connection':'close',
                'Accept':'*/*',
                'X-Requested-With':'XMLHttpRequest',
                'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350 Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36 JsKit/1.0 (Android);',
            }
            return scrapy.FormRequest(method='GET',url=url_comment,headers=headers,meta={'pre_data':metadata,'formdata':comment_next_params},callback=self.deal_comments,formdata=comment_next_params)
        return standard(metadata)