from datetime import datetime, timedelta

# get current day
current_date = datetime.now()
print(f'Today is {current_date}')

#days
one_day = timedelta(days=1)
yesterday = current_date - one_day
print(f'Yesterday was {yesterday}')

#weeks
one_week = timedelta(weeks=1)
last_week = current_date - one_week
print(f'Last week was {last_week}')

#formats
print(f'Day {current_date.day}')
print(f'Month {current_date.month}')
print(f'Year {current_date.year}')

print(f'Hour {current_date.hour}')
print(f'Minute {current_date.minute}')
print(f'Second {current_date.second}')