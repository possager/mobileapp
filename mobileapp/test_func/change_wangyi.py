import pymongo
import requests


# client1=pymongo.MongoClient('178.16.7.86',27017)
# COL1=client1['news']
# DOC1=COL1['channellist']


task_list=[
                {
                    'url':'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId':'T1457068979049',
                    'abstract':None,
                    'params':None,
                    'appname':'wangyi',
                    'channelName':'视频',
                    'request_data':{
                        'channel':'T1457068979049',
                        'subtab':'Video_Recom',
                        'size':'10',
                        'offset':'0',
                        'fn':'1',
                        'passport':'',
                        'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                        'lat':'',
                        'lon':'',
                        'version':'35.1',
                        'net':'wifi',
                        # 'ts':'1526776833',
                        # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                        # 'encryption':'1',
                        # 'canal':'news_lljc3',
                        'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                        'open':'',
                        'openpath':''
                    }
                },
                # {
                #     'url': 'http://c.m.163.com/recommend/getSubDocPic',
                #     'channelId': 'T1348647909107',
                #     'abstract': None,
                #     'params': None,
                #     'appname': 'wangyi',
                #     'channelName': '头条',
                #     'request_data':{
                #         'tid':'T1348647909107',
                #         'from':'toutiao',
                #         'offset':'20',
                #         'size':'10',
                #         'fn':'1',
                #         'LastStdTime':'1526756888',
                #         'spestr':'shortnews',
                #         'prog':'',
                #         # 'passport':'',
                #         'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                #         # 'lat':'',
                #         # 'lon':'',
                #         # 'version':'35.1',
                #         # 'net':'wifi',
                #         # 'ts':'1526773568',
                #         # 'sign':'Kr8H5/efevcqnpXLD6j4pyk/QKy7LsH5M0sslXNj5g148ErR02zJ6/KXOnxX046I',
                #         # 'encryption':'1',
                #         'canal':'news_lljc3',
                #         # 'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                #         # 'open':'',
                #         # 'openpath':''
                #     }
                # },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1467284926140',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '要闻',
                    'request_data':{
                            'from':'T1467284926140',
                            'size':'10',
                            'offset':'0',
                            'fn':'1',
                            'passport':'',
                            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                            'lat':'',
                            'lon':'',
                            'version':'35.1',
                            'net':'wifi',
                            # 'ts':'1526776833',
                            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                            # 'encryption':'1',
                            # 'canal':'news_lljc3',
                            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                            'open':'',
                            'openpath':''
                        }
                },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1348649580692',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '科技',
                    'request_data':{
                            'from':'T1348649580692',
                            'size':'10',
                            'offset':'0',
                            'fn':'1',
                            'passport':'',
                            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                            'lat':'',
                            'lon':'',
                            'version':'35.1',
                            'net':'wifi',
                            # 'ts':'1526776833',
                            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                            # 'encryption':'1',
                            # 'canal':'news_lljc3',
                            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                            'open':'',
                            'openpath':''
                        }
                },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1348648756099',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '财经',
                    'request_data':{
                            'from':'T1348648756099',
                            'size':'10',
                            'offset':'0',
                            'fn':'1',
                            'passport':'',
                            'devId':'iBqHGWB8Yx8XkfAf9bTKRw==',
                            'lat':'',
                            'lon':'',
                            'version':'35.1',
                            'net':'wifi',
                            # 'ts':'1526776833',
                            # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                            # 'encryption':'1',
                            # 'canal':'news_lljc3',
                            'mac':'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                            'open':'',
                            'openpath':''
                        }

                },
                {
                    'url': 'http://c.m.163.com/recommend/getSubDocPic',
                    'channelId': 'T1348648141035',
                    'abstract': None,
                    'params': None,
                    'appname': 'wangyi',
                    'channelName': '军事',
                    'request_data': {
                        'from': 'T1348648141035',
                        'size': '10',
                        'offset': '0',
                        'fn': '1',
                        'passport': '',
                        'devId': 'iBqHGWB8Yx8XkfAf9bTKRw==',
                        'lat': '',
                        'lon': '',
                        'version': '35.1',
                        'net': 'wifi',
                        # 'ts':'1526776833',
                        # 'sign':'Vu494rafuRoS2l0D7iED2MrT0Wprwf8FgssWwIQKURl48ErR02zJ6/KXOnxX046I',
                        # 'encryption':'1',
                        # 'canal':'news_lljc3',
                        'mac': 'Z8tAAqZCtjpSp6VxygeOyjC0ruPUyXM4Jwce4E9oM30=',
                        'open': '',
                        'openpath': ''
                    }

                },

            ]


for onechannel in task_list:
    # DOC1.insert(onechannel)
    print(onechannel)