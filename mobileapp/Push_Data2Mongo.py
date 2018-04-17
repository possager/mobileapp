import pymongo
import os
import sys
import json
import pymongo
import time



def scanf_file_store_data():
    basic_file='/Liang_Spider/spider_data_store/'
    os.chdir(basic_file)

    app_dir_root=os.listdir('.')

    #进入数据app文件夹目录
    for one_file in app_dir_root:
        app_name_path=basic_file+one_file+'/'
        os.chdir(app_name_path)

        all_date_dir=os.listdir(app_name_path)

        for one_date_dir in all_date_dir:
            if one_date_dir=='1111-11-11':
                continue

            app_name_date=app_name_path+one_date_dir+'/'
            all_app_data=os.listdir(app_name_date)

            for one_data in all_app_data:
                print(app_name_date+one_data)


def scanf_file_org_and_save():
    basic_file = '/Liang_Spider/spider_data_org/'
    # basic_file='E:/scrapy_data2/'
    os.chdir(basic_file)


    while True:
        all_data = os.listdir(basic_file)
        if len(all_data)>20:

            mongoclient = pymongo.MongoClient('178.16.7.86', 27017)
            # mongoclient=pymongo.MongoClient('127.0.0.1',27017)
            appCOL = mongoclient['news']
            newsdata = appCOL['news_content']



            print(all_data)
            for one_file in all_data:
                try:
                    one_org_file_path=basic_file+one_file
                    with open(one_org_file_path,'r') as fl:
                        datajson=json.load(fl)

                    #handle reply_nodes first
                    print('找到了一个数据，正在分析，推数据库')
                    print('正在将评论推送至数据库')
                    try:
                        if datajson['publish_time']=='1111-11-11 11:11:11':
                            try:
                                os.remove(one_org_file_path)
                            except Exception as e:
                                print(e)
                                return
                            continue
                        parent_id=datajson['id']
                        reply_nodes = datajson['reply_nodes']
                        appname=datajson['appname']
                        app_comment_db_name=appname+'_comment'
                        comment_db = appCOL[app_comment_db_name]

                        for n,one_reply in enumerate(reply_nodes):
                            one_reply['ancestor_id'] = parent_id
                            print('评论数量一gong ',len(reply_nodes),'ge','现在是第',n,'个')
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
                                print('更新了一个---------',_id1)
                            except Exception as e:
                                print('插入了一个---------',one_reply['content'])
                                comment_db.insert(one_reply)
                                pass
                        del datajson['reply_nodes']
                    except Exception as e:
                        print(one_file)
                        print(e)


                    #to ensure datajson dosen't contains reply_nodes
                    try:
                        del datajson['reply_nodes']
                    except Exception as e:
                        print(e)

                    #handle org_data secends
                    try:
                        result_cursor_content = newsdata.find({'urlmd5': datajson['urlmd5']})
                        count = result_cursor_content.count()
                        if count > 0:
                            _id2 = result_cursor_content[0]['_id']
                        else:
                            raise Exception

                        newsdata.update({'_id': _id2}, datajson)
                    except Exception as e:
                        newsdata.insert(datajson)
                        pass

                    #most importantly,delete this data
                    try:
                        os.remove(one_org_file_path)
                        print('删除一个')
                    except Exception as e:
                        print(e)
                        #return when wrong!avoid remaining pushing the same data to Mongo!
                        return
                except Exception as e:
                    print(e)
        else:
            time.sleep(60)





if __name__ == '__main__':
    # scanf_file()
    scanf_file_org_and_save()