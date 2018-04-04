# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from mobileapp.items import MobileappItem
import json
import os





BASIC_FILE='E:/data_ll_all/mobile_app/'

class MobileappPipeline(object):

    def process_item(self, item, spider):
        def save_data(file_path, file, full_data):  # 因为后来要用到存储的时候的文件名，先要调用里边的文件名，所以生成文件名和爬取数据结果应该分开写。
            if os.path.exists(file_path):
                with open(file, 'w+') as cmfl:
                    json.dump(full_data, cmfl)
            else:
                os.makedirs(file_path)
                with open(file, 'w+') as cmfl:
                    json.dump(full_data, cmfl)


        if isinstance(item,MobileappItem):
            item_dict=dict(item)
            save_data(file_path=BASIC_FILE+item_dict['appname'],file=item_dict['publish_time'],full_data=item_dict)



class setDefaultPipeline(object):
    def process_item(self,item,spider):
        for itemkey in item.fields:
            item.setdefault(itemkey,None)
        return item