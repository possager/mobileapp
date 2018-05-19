import pymongo
import time
import logging
import datetime




# logger=logging.getLogger(__name__)
# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# filehandler=logging.FileHandler('AdjustJRTTCmtNum.txt')
# filehandler.setLevel(logging.WARN)
# logger.addHandler(filehandler)

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("Proxy_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



while True:
    mongoclient = pymongo.MongoClient('178.16.7.86', 27017)
    appCOL = mongoclient['news']
    newsdata = appCOL['news_content']
    cmtDB=appCOL['jinritoutiao_comment']



    today_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))+' 00:00:00'
    num_total=newsdata.find({'appname':'jinritoutiao','publish_time':{'$gt':'2018-05-06 00:00:00'}}).count()
    print(num_total)
    for i in newsdata.find({'appname':'jinritoutiao','publish_time':{'$gt':'2018-05-06 00:00:00'}}):
        urlmd5_newsId=i['urlmd5']

        reply_count=cmtDB.find({'news_id':urlmd5_newsId}).count()
        newsdata.update({'_id':i['_id']},{'$set':{'reply_count':reply_count}},)
        logmsg='has adjusted a reoly_count in jinritoutiao_comment,id is %s,reply_count is %s'%(str(i['_id']),str(reply_count))
        logger.warning(msg=logmsg)

    mongoclient.close()



    timestampNow=time.time()
    timetuple=time.localtime(timestampNow)
    hournow=timetuple.tm_hour
    if hournow >12:
        timeStramp = time.time()
        datenow = datetime.datetime.today()
        tomarrow = (datenow + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
        tomarrowTuple = time.strptime(tomarrow, '%Y-%m-%d %H:%M:%S')
        tomarrowTupleStamp = time.mktime(tomarrowTuple)
        print(tomarrowTupleStamp)
        secendToSleep=tomarrowTupleStamp - timeStramp
        time.sleep(secendToSleep)
    else:
        timeStramp = time.time()
        datenow = datetime.datetime.today()
        tomarrow = datenow.strftime('%Y-%m-%d 12:00:00')
        tomarrowTuple = time.strptime(tomarrow, '%Y-%m-%d %H:%M:%S')
        tomarrowTupleStamp = time.mktime(tomarrowTuple)
        print(tomarrowTupleStamp)
        secendToSleep=tomarrowTupleStamp - timeStramp
        time.sleep(secendToSleep)
