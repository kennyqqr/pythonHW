import datetime, pytz, tzlocal

local_tz = tzlocal.get_localzone()
now, utcnow = datetime.datetime.now(), datetime.datetime.utcnow()
localnow = utcnow.replace(tzinfo=pytz.utc).astimezone(local_tz) 

print(local_tz)
print(now)
print(utcnow)
print(localnow)