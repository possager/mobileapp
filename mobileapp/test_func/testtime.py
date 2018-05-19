import time
import datetime
import logging
import pymongo



# timetuple=time.localtime(time.time())
# print(timetuple.tm_hour)

#
# timestramp=time.time()
# datenow=datetime.datetime.today()
# tomarrow=(datenow+datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
# tomarrow_tuple=time.strptime(tomarrow,'%Y-%m-%d %H:%M:%S')
# tomarrow_tuple_stamp=time.mktime(tomarrow_tuple)
# print(tomarrow_tuple_stamp)
# print(tomarrow_tuple_stamp-timestramp)

# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# logger=logging.getLogger(__name__)
# filehandler=logging.FileHandler('AdjustJRTTCmtNum.txt')
# filehandler.setLevel(logging.WARN)
# logger.addHandler(filehandler)
#
# logger.warning(msg='helloworld')

mongoclient = pymongo.MongoClient('localhost', 27017)
appCOL = mongoclient['appnewsMongodb']
newsdata = appCOL['newsdata_honghunaglan12_25_less1']
# jinritoutiaoComment=appCOL['jinritoutiao_comment']


print(newsdata.find().count())

for onenews in newsdata.find():
    newsdata.update({'_id':onenews['_id']},{'$Set':{'reply_count':50}})