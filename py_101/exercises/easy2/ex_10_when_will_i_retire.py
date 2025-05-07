from datetime import datetime

age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))

delta_years = retirement_age - age
year = datetime.now().year
retirement_year = year + delta_years

print(f"It's {year}. You will retire in {retirement_year}.")
print(f'You have only {delta_years} years of work to go!')