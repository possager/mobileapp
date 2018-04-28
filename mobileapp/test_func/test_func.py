import re


date_raw='2017年7月19日 11:25'

Re_find_date=re.compile('(\d{4}).*?(\d{1,2}).*?(\d{1,2}).*?(\d{1,2})\:(\d{1,2})')

result=Re_find_date.findall(date_raw)

print(result)