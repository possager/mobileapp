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
                'appname': one_board['appName'],
                'channelName': one_board['channelName'],
                'spider_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(time.time())))
            }
            yield scrapy.FormRequest(url=one_board_info['url'], headers=self.brownser_headers, meta={'pre_data': one_board_info},
                                     formdata=url1_dict,callback=self.deal_board,method='GET',dont_filter=True)
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


        def deal_comment_url(item_id):
            time_str = str(int(time.time() * 1000))
            url1_dict = {
                'group_id': item_id,
                'item_id': item_id,
                'aggr_type': '1',
                'count': '20',
                'offset': '0',
                'tab_index': '0',
                'fold': '1',
                'device_id': '51201841048',
                'iid': '30763638273',
                'ac': 'wifi',
                'channel': '360',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '666',
                'version_name': '6.6.6',
                'device_platform': 'android',
                # 'ab_version': '264037%2C308571%2C293032%2C283773%2C320329%2C317201%2C309312%2C319438%2C317498%2C318245%2C295827%2C325050%2C315441%2C239096%2C324283%2C170988%2C318440%2C320218%2C325197%2C265169%2C281390%2C297058%2C276203%2C286212%2C313219%2C313473%2C318242%2C312563%2C310595%2C325042%2C327128%2C322322%2C327760%2C317411%2C328093%2C323233%2C304133%2C326120%2C324799%2C317076%2C324571%2C280773%2C319962%2C326729%2C317208%2C322280%2C321405%2C326342%2C214069%2C319863%2C264033%2C258356%2C247849%2C280448%2C323844%2C281299%2C320995%2C325615%2C327725%2C326807%2C328053%2C287590%2C288418%2C290192%2C260657%2C327544%2C327894%2C326190%2C327181%2C324614%2C271178%2C326589%2C326524%2C326532',
                # 'ab_client': 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7',
                # 'ab_feature': '94563%2C102749',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': 'SM-G9350',
                'device_brand': 'samsung',
                'language': 'zh',
                'os_api': '22',
                'os_version': '5.1.1',
                'uuid': '865944459551126',
                'openudid': '7003041115949825',
                'manifest_version_code': '666',
                'resolution': '1280*720',
                'dpi': '192',
                'update_version_code': '66611',
                '_rticket': time_str,
                'plugin': '10607',
                # 'fp': 'z2TqPlP_LlG7FlPrLlU1FYK7FYFI',
                # 'pos': '5r_88Pzt3vTp5L-nv3sVDXQeIHglH7-xv_zw_O3R8vP69Ono-fi_p6ytqbOtq6upqKuxv_zw_O3R_On06ej5-L-nrq2zq6yvqKyu4A%3D%3D',
                # 'rom_version': '22',
                # 'ts': '1524551666',
                # 'as': 'a2d54ccd928ffabf3e7240',
                # 'mas': '0071fa1278a41b230146db84092b54cdcd0aa2628e8ae0c698',
                # 'odin_tt':'dc611ac46faf1607054b116a96100182592497ca4c4c7f7e2ab9d3bc5174210005f3061297bf55728f26bccaf03c0652',
                # 'qh[360]':'1',
                # 'install_id':'30763638273',
                # 'ttreq':'1$822f55234ceb355b3d20cbab3f24ec4adc299e2e',
            }

            return url1_dict


        datajson=json.loads(response.text)

        try:
            content=datajson['data']['content']
        except Exception as e:
            print(e)
        publish_user_id=datajson['data']['creator_uid']
        try:
            publish_user=datajson['data']['media_user']['screen_name']
            publish_user_photo = datajson['data']['media_user']['avatar_url']
            source=datajson['data']['source']
        except Exception as e:
            print(e)
            publish_user=datajson['data']['creator_uid']
            publish_user_photo=None
            source=datajson['data']['source']


        selector1=scrapy.Selector(text=content)
        img_urls=selector1.xpath('//img/@src').extract()

        content_dict={
            'content':content,
            'publish_user_id':publish_user_id,
            'img_urls':img_urls,
            'publish_user_photo':publish_user_photo,
            'publish_user':publish_user,
            'source':source
        }
        metadata.update(content_dict)

        comment_params=deal_comment_url(item_id=metadata['item_id'])
        comment_url_v2='https://iu.snssdk.com/article/v2/tab_comments/'
        xssreqticket_str=str(time.time()*1000)
        headers_for_comment_url={
            'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9350 Build/LMY48Z) NewsArticle/6.6.6 okhttp/3.7.0.6',
            'Host':'iu.snssdk.com',
            'Connection':'close',
            'X-SS-REQ-TICKET':xssreqticket_str,
                }

        yield scrapy.FormRequest(method='GET',url=comment_url_v2,meta={'pre_data':metadata},callback=self.deal_comments,formdata=comment_params,headers=headers_for_comment_url,dont_filter=True)










        # return scrapy.FormRequest(url=url_cmt,headers=self.mobile_app_headers,meta={'pre_data':metadata,'formdata':formdata},formdata=formdata,callback=self.deal_comments)




    def deal_comments(self,response):
        metadata=response.meta['pre_data']


        def deal_publish_time(publicTimestamp):
            time_tuple=time.localtime(int(publicTimestamp))
            time2=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
            return time2

        # def deal_commentUrl_next(comment_url):
        #     comment_url_splited=comment_url.split('offset=')
        #     pageNum=int(comment_url_splited[1])
        #     pageNum+=20
        #     comment_url_next=comment_url_splited[0]+'offset='+str(pageNum)
        #     return comment_url_next

        def deal_comment_next_params(item_id,response):
            time_str = str(int(time.time() * 1000))
            offset=response.url.split('offset=')[1].split('&')[0]
            offset=int(offset)
            url1_dict = {
                'group_id': item_id,
                'item_id': item_id,
                'aggr_type': '1',
                'count': '20',
                'offset': str(offset+20),
                'tab_index': '0',
                'fold': '1',
                'device_id': '51201841048',
                'iid': '30763638273',
                'ac': 'wifi',
                'channel': '360',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '666',
                'version_name': '6.6.6',
                'device_platform': 'android',
                # 'ab_version': '264037%2C308571%2C293032%2C283773%2C320329%2C317201%2C309312%2C319438%2C317498%2C318245%2C295827%2C325050%2C315441%2C239096%2C324283%2C170988%2C318440%2C320218%2C325197%2C265169%2C281390%2C297058%2C276203%2C286212%2C313219%2C313473%2C318242%2C312563%2C310595%2C325042%2C327128%2C322322%2C327760%2C317411%2C328093%2C323233%2C304133%2C326120%2C324799%2C317076%2C324571%2C280773%2C319962%2C326729%2C317208%2C322280%2C321405%2C326342%2C214069%2C319863%2C264033%2C258356%2C247849%2C280448%2C323844%2C281299%2C320995%2C325615%2C327725%2C326807%2C328053%2C287590%2C288418%2C290192%2C260657%2C327544%2C327894%2C326190%2C327181%2C324614%2C271178%2C326589%2C326524%2C326532',
                # 'ab_client': 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7',
                # 'ab_feature': '94563%2C102749',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': 'SM-G9350',
                'device_brand': 'samsung',
                'language': 'zh',
                'os_api': '22',
                'os_version': '5.1.1',
                'uuid': '865944459551126',
                'openudid': '7003041115949825',
                'manifest_version_code': '666',
                'resolution': '1280*720',
                'dpi': '192',
                'update_version_code': '66611',
                '_rticket': time_str,
                'plugin': '10607',
                # 'fp': 'z2TqPlP_LlG7FlPrLlU1FYK7FYFI',
                # 'pos': '5r_88Pzt3vTp5L-nv3sVDXQeIHglH7-xv_zw_O3R8vP69Ono-fi_p6ytqbOtq6upqKuxv_zw_O3R_On06ej5-L-nrq2zq6yvqKyu4A%3D%3D',
                # 'rom_version': '22',
                # 'ts': '1524551666',
                # 'as': 'a2d54ccd928ffabf3e7240',
                # 'mas': '0071fa1278a41b230146db84092b54cdcd0aa2628e8ae0c698',
            }
            return url1_dict

        try:
            datajson = json.loads(response.text)
            has_more=datajson['has_more']
        except Exception as e:
            print(e)
            return standard(metadata)


        if len(datajson['data'])<2:
            stand_data= standard(metadata)
            # print(datajson)
            print('this is datajson"s content ahead')
            print('the urlmd5 is'+stand_data['urlmd5'])

            return stand_data


        for one_cmt in datajson['data']:
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

        comment_params_next=deal_comment_next_params(metadata['id'],response)
        comment_url_v2='https://iu.snssdk.com/article/v2/tab_comments/'
        xssreqticket_str=str(time.time()*1000)
        headers_for_comment_url = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9350 Build/LMY48Z) NewsArticle/6.6.6 okhttp/3.7.0.6',
            'Host': 'iu.snssdk.com',
            'Connection': 'close',
            'X-SS-REQ-TICKET': xssreqticket_str,
        }

        if has_more:
            return scrapy.FormRequest(method='GET',url=comment_url_v2,meta={'pre_data':metadata},callback=self.deal_comments,headers=headers_for_comment_url,formdata=comment_params_next,dont_filter=True)
        else:
            stand_data = standard(metadata)
            print('in bottom,the urlmd5 is' + stand_data['urlmd5'])
            return stand_data
            # yield standard(metadata)