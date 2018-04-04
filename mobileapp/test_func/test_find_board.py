import pymongo
import requests
import re




mongoclient=pymongo.MongoClient('178.16.7.86',27017)
COL=mongoclient['news']
DCO=COL['channellist']

mongofind=DCO.find({'appName':'thepaper','recommend':{'$gt':0}})
url=mongofind[0]['url']


response1=requests.get(url=url)
# print(response1.text)
Re_pattern = re.compile(r'data	:	\"(.*?)\".*?Math\.random\b')
datare = Re_pattern.findall(response1.text)
print(datare)