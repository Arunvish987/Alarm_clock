import os
import datetime
import time

n = 1
c, b, a = input('Enter the Date = ').split('/')
hr, minn, sec = input('Enter the time = ').split(':')
schedule_date = datetime.date(int(a), int(b), int(c))
while n>0:
    if time.localtime().tm_hour==int(hr) and time.localtime().tm_min==int(minn) and time.localtime().tm_sec==int(sec):
        os.startfile('C:\\Users\\arun\\Desktop\\pyar.mp3')      #enter the file path eg.music file
        break
    else:
        n+=1