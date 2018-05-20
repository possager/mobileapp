import requests
from scrapy.selector import Selector
import json



cmt_url='https://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/DI8G906G0001875P/app/comments/newList?offset=20&limit=20&showLevelThreshold=5&headLimit=3&tailLimit=2'

cmt_url_host='https://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/DI8G906G0001875P/app/comments/newList'

params={
    'offset':'2000',
    'limit':'20',
    'showLevelThreshold':'5',
    'headLimit':'3',
    'tailLimit':'2',
}



headers={
    'Accept-Encoding':'gzip',
    'Connection':'Keep-Alive',
    'Host':'comment.api.163.com',
    'X-NR-Trace-Id':'1526813455392_951419013_863213510134567',
    'User-Agent':'NewsApp/35.1 Android/5.1.1 (samsung/SM-G9350)',
    'User-C':'6KaB6Ze7',
    'User-N':'wKq3+ZhKJshqLUdmuO/3GU54yPhI0ZGYXNBL+qbp+gYtkyOvjJ64oHfDp3tOH9cB'
}


response1=requests.get(url=cmt_url_host,headers=headers,params=params)
print(response1.status_code)
print(response1.text)

datajson=json.loads(response1.text)
# comment_list=datajson['comments']
#
# for one_comment in comment_list.keys():
#     print(comment_list[one_comment]['content'])