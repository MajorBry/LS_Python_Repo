from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()

print(repr(today_year))
print(repr(iso_year))