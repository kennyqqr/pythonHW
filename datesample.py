import datetime

now = datetime.datetime.now()
tbdate = datetime.datetime(2018,12,15)

print(now)
print(now.year)
print(now.strftime("%A"))
print(tbdate)
print(now.strftime("%Y/%m/%d %H:%M:%S"))