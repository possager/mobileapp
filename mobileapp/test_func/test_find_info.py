# import pymongo
#
#
#
# client=pymongo.MongoClient('178.16.7.86',27017)
#
# COL1=client['news']
# DOC1=COL1['channellist']
#
# COL2=client['test1']
# DOC2=COL2['channellist']
#
#
# for one_channellist_info in DOC1.find({'appName':'wangyi'}):
#     DOC2.insert(dict(one_channellist_info))