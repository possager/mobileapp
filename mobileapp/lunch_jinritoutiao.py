#_*_coding:utf-8_*_
import requests
import json
import time

#临时添加，因为大领导经常看。所以要多跑跑。
console_url='http://127.0.0.1:6800'
# console_url='http://178.16.7.121:6800'#remote


def start_a_spider_job(project='default',spidername=None):
    if spidername:
        spider_task={
            'project':project,
            'spider':spidername,
            'setting':None,
            'jobid':None
        }
        respons1=requests.post(url=console_url+'/schedule.json',data=spider_task)
        print(respons1.text)

    else:
        print('请输入一个正确的爬虫名称')


if __name__ == '__main__':
    while True:
        start_a_spider_job(spidername='jinritoutiao')
        time.sleep(30*60)
