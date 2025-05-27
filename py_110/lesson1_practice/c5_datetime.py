from datetime import datetime as dt

date = dt.strptime("July 16, 2022", "%B %d, %Y")
weekday_name = date.strftime('%A')
print(weekday_name)                   # Saturday
