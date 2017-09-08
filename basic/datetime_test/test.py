import os
import datetime
import time

print(time.time())


print(datetime.datetime.now().time())
timenow = datetime.datetime.now().time()
print(timenow)
save_time = "1:3:4"
timeprev = datetime.datetime.strptime(save_time, '%H:%M:%S').time()
print(timeprev)
subtract_time = timenow.hour*3600+timenow.minute*60+timenow.second - (
	timeprev.hour*3600+timeprev.minute*60+timeprev.second)
print(subtract_time)
