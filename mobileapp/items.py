# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class MobileappItem(scrapy.Item):


    #app项目中独有的字段
    appname=scrapy.Field()
    user_from=scrapy.Field()
    channelName=scrapy.Field()
    channelId=scrapy.Field()
    publicTimestamp=scrapy.Field()#public是什么鬼？10位的时间戳
    urlmd5=scrapy.Field()





    title = scrapy.Field()  # 标题
    content = scrapy.Field()  # 去噪后的存文本内容
    spider_time = scrapy.Field()  # 爬虫爬取时间
    publish_time = scrapy.Field()  # 发布时间
    id = scrapy.Field()  # 在平台中的言论ID（如果是回复的话，有就填，没有就不填）
    publish_user = scrapy.Field()  # 用户名-----------------------------------------------------------------------------!!!!!
    url = scrapy.Field()  # （论坛的URL）||（论坛回复的URL）||（新闻的URL）


    img_urls = scrapy.Field()  # 图片urls,string数组类型
    publish_user_id = scrapy.Field()  # 用户id
    reply_count = scrapy.Field()  # 回复数

    publish_user_photo = scrapy.Field()  # 用户头像
    read_count = scrapy.Field()  # 阅读量
    like_count = scrapy.Field()  # 赞成数
    publish_user_jsonid = scrapy.Field()  # 用户的jsonid(对应着用户json信息的命名：平台名称（或者英文）_用户id)
    txpath = scrapy.Field()  # 图片存放服务器(针对微信)
    reply_nodes = scrapy.Field()  # jsonArray类型变量,结构和当前json结构一样
    reproduce_count = scrapy.Field()  # 转载数
    ancestor_id = scrapy.Field()  # 祖先借点的ID（回复和回复的回复必填）
    parent_id = scrapy.Field()  # 父集ID（如果是回复就填，没有就不填）
    like_nodes = scrapy.Field()  # jsonArray类型变量，里面的结构和当前json结构一样
    video_urls = scrapy.Field()  # 视频urls,string数组类型
    is_pic = scrapy.Field()  # 是否包含图片(针对微信)
    dislike_count = scrapy.Field()  # 反对数
    params=scrapy.Field()


class mobileAppUserInfo(scrapy.Field):
    publish_user = scrapy.Field(output_processor=TakeFirst())  # 用户名
    publish_user_photo = scrapy.Field(output_processor=TakeFirst())  # 用户头像
    publish_user_id = scrapy.Field(output_processor=TakeFirst())  # 发布用户Id
    url = scrapy.Field(output_processor=TakeFirst())  # 用户主页Url
    fans_count = scrapy.Field(output_processor=TakeFirst())  # 粉丝数量
    follow_count = scrapy.Field(output_processor=TakeFirst())  # 关注数量
    friend_count = scrapy.Field(output_processor=TakeFirst())  # 好友数量
    sex = scrapy.Field(output_processor=TakeFirst())  # 性别
    register_time = scrapy.Field(output_processor=TakeFirst())  # 注册时间
    article_count = scrapy.Field(output_processor=TakeFirst())  # 发帖数（微博数、主题数）
    reply_article_count = scrapy.Field(output_processor=TakeFirst())  # 回帖数量
    visit_count = scrapy.Field(output_processor=TakeFirst())  # 主页访问数量
    group_name = scrapy.Field()  # 用户所属组
    introduction = scrapy.Field(output_processor=TakeFirst())  # 签名或者简介
    fans_details = scrapy.Field()  # 包含字段[id,用户名，头像，账户主页]
    follow_details = scrapy.Field()  # 包含字段[id,用户名，头像，账户主页]
    friend_details = scrapy.Field()  # 包含字段[id,用户名，头像，账户主页]
