# from scrapy.spiders import Spider
# import scrapy
# import time
# from random import randint
#
#
#
#
#
# class test_spider(Spider):
#     name = 'test_spider'
#     start_urls=[
#         'https://www.mala.cn/forum-70-{}.html'.format(str(i)) for i in range(1,50)
#     ]
#
#
#     headers1={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#         'Upgrade-Insecure-Requests':'1',
#         'Host':'www.mala.cn',
#         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Accept-Encoding':'gzip, deflate, br',
#     }
#
#     def start_requests(self):
#         for one_url in self.start_urls[:20]:
#             yield scrapy.Request(url=one_url,headers=self.headers1,callback=self.deal_index_next)
#         # return scrapy.Request(url=self.start_urls[2],headers=self.headers1)
#
#     def deal_index_next(self,response):
#         print('in deal_index_next!!!,url is in behind')
#         print(response.url)
#
#
#         index_dict={
#             'url':response.url,
#             'time':time.time(),
#         }
#
#         randint_num=randint(0,10)
#
#         index_dict['random_num'] = randint_num
#         if randint_num<5:
#
#             yield index_dict
#         elif randint_num<9:
#             yield index_dict
#         else:
#             return scrapy.Request(url='http://www.baidu.com',headers=self.headers1,callback=self.deal_index_next)
