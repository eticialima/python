from datetime import datetime, timedelta
 
current_date = datetime.now()
print(current_date)
 
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))
 
date_entered = input('Please enter a date (dd/mm/yyyy): ')
date_entered = datetime.strptime(date_entered, '%d/%m/%Y')
 
one_week = timedelta(weeks=1)
one_week_later = date_entered + one_week
print('One week later it will be: ' + str(one_week_later))