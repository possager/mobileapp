import time
import datetime


# timetuple=time.localtime(time.time())
# print(timetuple.tm_hour)


timestramp=time.time()
datenow=datetime.datetime.today()
tomarrow=(datenow+datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
tomarrow_tuple=time.strptime(tomarrow,'%Y-%m-%d %H:%M:%S')
tomarrow_tuple_stamp=time.mktime(tomarrow_tuple)
print(tomarrow_tuple_stamp)
print(tomarrow_tuple_stamp-timestramp)