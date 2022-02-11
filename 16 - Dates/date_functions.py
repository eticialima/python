from datetime import datetime, timedelta

today = datetime.now()

print('Today is: ' + str(today)) 
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))

