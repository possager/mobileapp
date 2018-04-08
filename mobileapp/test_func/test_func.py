from hashlib import md5


url=u'http://image.thepaper.cn/image/7/220/187.jpg'

print(md5(str(url).encode('utf-8')).hexdigest())