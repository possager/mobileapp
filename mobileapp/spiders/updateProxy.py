#_*_coding:utf-8_*_
from scrapy.spiders import Spider
import scrapy


# class updateProxy(Spider):
#     name = 'updateProxy'
#
#
#     headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#         'Upgrade-Insecure-Requests':'1',
#         'Accept-Language':'zh-CN,zh;q=0.9',
#         'Accept-Encoding':'gzip, deflate',
#         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
#     }
#
#     def start_requests(self):
#         xiciurlList=['http://www.xicidaili.com/nt/{}'.format(str(i)) for i in range(1,10)]#国内透明代理
#         for onexiciurl in xiciurlList:
#             yield scrapy.Request(url=onexiciurl,headers=self.headers,callback=self.deal_content,meta={})
#
#
#     def deal_content(self,response):