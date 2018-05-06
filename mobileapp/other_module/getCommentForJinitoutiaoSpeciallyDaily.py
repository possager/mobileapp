import pymongo
import time
import requests




mongoclient = pymongo.MongoClient('178.16.7.86', 27017)
appCOL = mongoclient['news']
newsdata = appCOL['news_content']
jinritoutiaoComment=appCOL['jinritoutiao_comment']


def getDataFromMongo(beginDate):
    for oneNews in newsdata.find({'appname':'jinritoutiao','publish_time':{'$gt':beginDate}}):
        _id=str(oneNews['id'])

        timestr=str(time.time()*1000)
        comment_dict={
            'group_id': _id,
            'item_id': _id,
            'aggr_type': '1',
            'count': '20',
            'offset': 0,
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
            '_rticket': timestr,
            'plugin': '10607',
        }

        yield comment_dict,dict(oneNews)



def getComment(commentDict):
    commentList=[]


    def deal_publish_time(publicTimestamp):
        time_tuple = time.localtime(int(publicTimestamp))
        time2 = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
        return time2

    def deal_comment_next_params(item_id, response):
        time_str = str(int(time.time() * 1000))
        offset = response.url.split('offset=')[1].split('&')[0]
        offset = int(offset)
        url1_dict = {
            'group_id': item_id,
            'item_id': item_id,
            'aggr_type': '1',
            'count': '20',
            'offset': str(offset + 20),
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


    xssreqticket_str = str(time.time() * 1000)
    headers_for_comment_url = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9350 Build/LMY48Z) NewsArticle/6.6.6 okhttp/3.7.0.6',
        'Host': 'iu.snssdk.com',
        'Connection': 'close',
        'X-SS-REQ-TICKET': xssreqticket_str,
    }

    try:
        response1=requests.get(url='https://iu.snssdk.com/article/v2/tab_comments/',headers=headers_for_comment_url,params=commentDict)
        datajson=response1.json()
        hasmore=datajson['has_more']
    except Exception as e:
        return commentList

    if len(datajson['data']) < 2:
        return commentList

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


        ancestor_id = commentDict['item_id']
        parent_id = commentDict['item_id']




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
        commentList.append(one_cmt_dict)

    if hasmore:
        time.sleep(2)
        nextCommentDict=deal_comment_next_params(commentDict['item_id'],response1)
        commentList=commentList+getComment(nextCommentDict)



    return commentList


def sendCommentDictToMongo():
    for i,j in getDataFromMongo('2018-05-06 00:00:00'):
        commentDict=getComment(i)
        datajson=j

        try:
            if datajson['publish_time'] == '1111-11-11 11:11:11':
                continue
            parent_id = datajson['id']
            reply_nodes = commentDict
            appname = datajson['appname']
            app_comment_db_name = appname + '_comment'
            comment_db = appCOL[app_comment_db_name]

            for n, one_reply in enumerate(reply_nodes):
                one_reply['ancestor_id'] = parent_id
                print('评论数量一gong ', len(reply_nodes), 'ge', '现在是第', n, '个')
                print('')
                one_reply['news_id'] = datajson['urlmd5']
                one_reply['publish_user_id'] = parent_id
                try:
                    result_cursor = comment_db.find(
                        {'news_id': one_reply['news_id'], 'publish_user': one_reply['publish_user']})
                    count = result_cursor.count()
                    if count > 0:
                        _id1 = result_cursor[0]['_id']
                    else:
                        raise Exception
                    comment_db.update({'_id': _id1}, one_reply)
                    print('更新了一个---------', _id1)
                except Exception as e:
                    print('插入了一个---------', one_reply['content'])
                    comment_db.insert(one_reply)
                    pass
            del datajson['reply_nodes']
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # for i in getDataFromMongo('2018-05-06 00:00:00'):
    #     getComment(i)
    sendCommentDictToMongo()