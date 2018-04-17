# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from mobileapp.items import MobileappItem
import json
import os
import platform




basic_file = 'E:/scrapy_data/'
basic_file_org='E:/scrapy_data2'
if platform.system() == 'Linux':
    basic_file = '/Liang_Spider/spider_data_store/'
    basic_file_org='/Liang_Spider/spider_data_org'



class MobileappPipeline(object):

    def process_item(self, item, spider):
        def save_data_store(file_path, file, full_data):  # 因为后来要用到存储的时候的文件名，先要调用里边的文件名，所以生成文件名和爬取数据结果应该分开写。

            publish_date=file.split(' ')[0]
            filename=full_data['appname']+'_'+full_data['urlmd5']


            file_path_new=file_path+'/'+publish_date
            file_path_and_name=file_path_new+'/'+filename





            if os.path.exists(file_path_new):
                with open(file_path_and_name, 'w+') as cmfl:
                    json.dump(full_data, cmfl)
            else:
                os.makedirs(file_path_new)
                with open(file_path_and_name, 'w+') as cmfl:
                    json.dump(full_data, cmfl)

        def save_data_org(full_data):
            filename = full_data['appname'] + '_' + full_data['urlmd5']
            with open(basic_file_org+'/'+filename,'w+') as fl:
                json.dump(full_data,fl)


        if isinstance(item,MobileappItem):
            item_dict=dict(item)
            save_data_store(file_path=basic_file+item_dict['appname'],file=item_dict['publish_time'],full_data=item_dict)
            save_data_org(full_data=item_dict)




class setDefaultPipeline(object):
    def process_item(self,item,spider):
        for itemkey in item.fields:
            item.setdefault(itemkey,None)
        return item


class testpipelineNum(object):
    def process_item(self,item,spider):
        print('has got one itme',item['url'])