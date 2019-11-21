import datetime

datetime_object = datetime.date.today()
print(datetime_object.day)
print(datetime_object.month)
print(datetime_object.year)


from datetime import datetime
d = datetime(1,1,1).now()

print(d)

print('{}:{:02d} {}/{}/{}'.format(d.hour,d.minute,d.month,d.day,d.year))