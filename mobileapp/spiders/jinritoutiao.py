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
from mobileapp.other_module.execjs_cal_as_cp_for_JinRiTouTiao import caculate_as_cp





class jinritoutiao(Spider):
    name = 'jinritoutiao'



    brownser_headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        'Referer':'https://m.toutiao.com/?w2atif=1&channel=news_hot',
        'Host':'m.toutiao.com',
        'Connection':'close',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept':'*/*'
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
        #             'url': 'https://m.toutiao.com/list/',
        #             'channelId': 'news_hot',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'jinritoutiao',
        #             'channelName': '热点'
        #         },
        #         {
        #             'url': 'https://m.toutiao.com/list/',
        #             'channelId': 'news_local',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'jinritoutiao',
        #             'channelName': '成都'
        #         },
        #         {
        #             'url': 'https://m.toutiao.com/list/',
        #             'channelId': 'news_society',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'jinritoutiao',
        #             'channelName': '社会'
        #         },
        #         {
        #             'url': 'https://m.toutiao.com/list/',
        #             'channelId': 'news_tech',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'jinritoutiao',
        #             'channelName': '科技'
        #         },
        #         {
        #             'url': 'https://m.toutiao.com/list/',
        #             'channelId': 'news_finance',
        #             'abstract': None,
        #             'params': None,
        #             'appname': 'jinritoutiao',
        #             'channelName': '财经'
        #         },
        #     ]
        #     for one_task in task_list[:1]:
        #         as_cp = caculate_as_cp()
        #         time_str = str(int(time.time()))
        #         url1_dict = {
        #             'tag': 'news_hot',
        #             'ac': 'wap',
        #             'count': '20',
        #             'format': 'json_raw',
        #             'as': as_cp['as'],
        #             'cp': as_cp['cp'],
        #             'max_behot_time': time_str,
        #             # '_signature':'kkyhfgAAyI04Y-H-xSTfTZJMoW',
        #             '_signature': time_str,
        #             'i': time_str
        #         }
        #
        #         yield scrapy.FormRequest(url=one_task['url'], headers=self.brownser_headers, meta={'pre_data': one_task},formdata=url1_dict,
        #                                   callback=self.deal_board,method='GET')
        # for i in get_request_for_debug():
        #     yield i

        client=pymongo.MongoClient('178.16.7.86',27017)
        COL=client['news']
        DOC=COL['channellist']

        mongocfg=DOC.find({'appName':'jinritoutiao','recommend':{'$gt':0}})
        for one_board in mongocfg:
            as_cp = caculate_as_cp()
            time_str = str(int(time.time()))
            url1_dict = {
                'tag': 'news_hot',
                'ac': 'wap',
                'count': '20',
                'format': 'json_raw',
                'as': as_cp['as'],
                'cp': as_cp['cp'],
                'max_behot_time': time_str,
                # '_signature':'kkyhfgAAyI04Y-H-xSTfTZJMoW',
                '_signature': time_str,
                'i': time_str
            }


            one_board_info = {
                'url': 'https://m.toutiao.com/list/',
                'channelId': one_board['channelId'],
                'abstract': None,
                'params': None,
                'appname': 'thepaper',
                'channelName': one_board['channelName']
            }
            yield scrapy.FormRequest(url=one_board_info['url'], headers=self.brownser_headers, meta={'pre_data': one_board_info},
                                     formdata=url1_dict,callback=self.deal_board,method='GET')
        client.close()



    def deal_board(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publish_time_raw):
            if len(publish_time_raw)<19:
                return publish_time_raw+':00'

        def deal_url_for_content(article_id):
            return 'https://m.toutiao.com/i'+article_id+'/info/'


        board_reponse_json=json.loads(response.text)


        for one_article in board_reponse_json['data']:
            metadata_in_for=copy.copy(metadata)

            title=one_article['title']
            url=one_article['display_url']
            abstract=one_article['abstract']
            reply_count=one_article['comment_count']
            publish_time_raw=one_article['datetime']
            params={
                'keywords':one_article['keywords'] if 'keywords' in one_article.keys() else None,
                'source_url':one_article['article_url'] if 'article_url' in one_article.keys() else None,
                'tag':one_article['tag'] if 'tag' in one_article.keys() else None,
                'ban_comment':one_article['ban_comment'] if 'ban_comment' in one_article.keys() else None
            }
            source=one_article['source']
            publicTimestamp=one_article['publish_time']
            _id=one_article['group_id']
            item_id=one_article['item_id']

            publish_time=deal_publish_time(publish_time_raw)


            one_article_dict={
                'title':title,
                'url':url,
                'abstract':abstract,
                'reply_count':reply_count,
                'publish_time':publish_time,
                'params':params,
                'source':source,
                'publicTimestamp':publicTimestamp,
                'id':_id,
                'item_id':item_id
            }
            metadata_in_for.update(one_article_dict)

            url_for_content=deal_url_for_content(metadata_in_for['id'])

            yield scrapy.Request(url=url_for_content,headers=self.brownser_headers,meta={'pre_data':metadata_in_for},callback=self.deal_content)










    def deal_content(self,response):
        metadata=response.meta['pre_data']
        metadata['reply_nodes']=[]


        def deal_comment_url(article_id,item_id):
            comment_url_20='http://ic.snssdk.com/article/v1/tab_comments/?group_id='+article_id+'&item_id='+str(item_id)+'&aggr_type=1&count=20&offset=0'
            return comment_url_20


        datajson=json.loads(response.text)


        content=datajson['data']['content']
        publish_user_id=datajson['data']['creator_uid']
        publish_user=datajson['data']['media_user']['screen_name']
        publish_user_photo=datajson['data']['media_user']['avatar_url']

        selector1=scrapy.Selector(text=content)
        img_urls=selector1.xpath('//img/@src').extract()

        content_dict={
            'content':content,
            'publish_user_id':publish_user_id,
            'img_urls':img_urls,
            'publish_user_photo':publish_user_photo,
            'publish_user':publish_user
        }
        metadata.update(content_dict)

        url_for_comments=deal_comment_url(article_id=metadata['id'],item_id=metadata['item_id'])


        yield scrapy.Request(url=url_for_comments,meta={'pre_data':metadata},callback=self.deal_comments)










        # return scrapy.FormRequest(url=url_cmt,headers=self.mobile_app_headers,meta={'pre_data':metadata,'formdata':formdata},formdata=formdata,callback=self.deal_comments)




    def deal_comments(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publicTimestamp):
            time_tuple=time.localtime(int(publicTimestamp))
            time2=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
            return time2

        def deal_commentUrl_next(comment_url):
            comment_url_splited=comment_url.split('offset=')
            pageNum=int(comment_url_splited[1])
            pageNum+=20
            comment_url_next=comment_url_splited[0]+'offset='+str(pageNum)
            return comment_url_next


        datajson = json.loads(response.text)
        has_more=datajson['has_more']


        if len(datajson['data'])<2:
            stand_data= standard(metadata)
            print('the urlmd5 is'+stand_data['urlmd5'])

            return stand_data


        for one_cmt in datajson['data'][1:]:
            one_cmt=one_cmt['comment']
            id = one_cmt['id']
            content = one_cmt['text']
            reply_count=one_cmt['reply_count']
            params={
                'bury_count':one_cmt['bury_count'],
            }
            publicTimestamp=one_cmt['create_time']
            publish_user_id = one_cmt['user_id']
            publish_user = one_cmt['user_name']
            like_count = one_cmt['digg_count']  # like_count
            publish_user_photo = one_cmt['user_profile_image_url']


            ancestor_id = metadata['id']  #
            parent_id = metadata['id']




            publish_time=deal_publish_time(publicTimestamp)


            one_cmt_dict = {
                'id': id,
                'publicTimestamp':publicTimestamp,
                'content': content,
                'publish_usr_id': publish_user_id,
                'publish_user': publish_user,
                'like_count': like_count,
                'publish_time': publish_time,
                'publish_user_photo': publish_user_photo,
                'ancestor_id': ancestor_id,
                'parent_id': parent_id,
                'reply_count':reply_count,
                'params':params,
            }
            metadata['reply_nodes'].append(one_cmt_dict)

        urlnext=deal_commentUrl_next(response.url)

        if has_more:
            return scrapy.Request(url=urlnext,meta={'pre_data':metadata},callback=self.deal_comments)
        else:
            stand_data = standard(metadata)
            print('in bottom,the urlmd5 is' + stand_data['urlmd5'])
            return stand_data
            # yield standard(metadata)