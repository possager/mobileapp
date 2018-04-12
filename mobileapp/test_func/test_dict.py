import time


time1_str='1523389540'

timetuple=time.localtime(int(time1_str))
print(timetuple)
time2=time.mktime(timetuple)
print(time2)
print(time.strftime('%Y-%m-%d %H:%M:%S',timetuple))