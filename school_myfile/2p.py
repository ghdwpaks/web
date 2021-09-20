import datetime
t = datetime.date.today()
w = datetime.timedelta(weeks=1)


next_week = t + w
print("오늘 :",t)
print("일주일 후 :",next_week)