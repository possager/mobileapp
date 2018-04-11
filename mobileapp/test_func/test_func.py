import requests

brownser_headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        'Referer':'https://m.toutiao.com/?w2atif=1&channel=news_hot',
        'Host':'m.toutiao.com',
        'Connection':'close',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept':'*/*'
    }

url_for_comment='http://ic.snssdk.com/article/v1/tab_comments/?group_id=6542822021913379342&item_id=6542822021913379342&aggr_type=1&count=20&offset=20&tab_index=0&iid=30356753779&device_id=50873777306&ac=wifi&channel=xiaozhi_lite36&aid=35&app_name=news_article_lite&version_code=625&version_name=6.2.5&device_platform=android&ab_client=a1%2Cc2%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=z1&ab_feature=z1&abflag=3&ssmix=a&device_type=HUAWEI+MLA-AL10&device_brand=HUAWEI&language=zh&os_api=19&os_version=4.4.2&uuid=863064010086264&openudid=0862667c7ee13094&manifest_version_code=625&resolution=1280*720&dpi=240&update_version_code=6257&_rticket=1523437836003&rom_version=19&fp=PlTqcWFtLlceFlPrPlU1FlFeFzwb&ts=1523437836&as=l29171d5cd6cdcf0ba81ed&mas=00d392e60c6d4652cb690e079a7f4f0c63628eea7c4566442c'
url_for_comment2='http://ic.snssdk.com/article/v1/tab_comments/?group_id=6542822021913379342&item_id=6542822021913379342&aggr_type=1&count=20&offset=40'

response1=requests.get(url=url_for_comment2)
print(response1.text)
print()