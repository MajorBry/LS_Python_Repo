"""
Problem:  write a function that determines how many Friday the 13ths are in a specific year
    Input:  integer, year (Gregorian)
    Output:  integer, number of 13-Fridays
    Rules
        Explicit
            - assume year is after 1752 and gregorian calendar use will continue in perpetuity
        Implicit
            - There is a maximum of 12 days possible
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - Assume I'm going to have to use the datetime module
"""
import datetime

def friday_the_13ths(year):
    friday_13ths = 0
    for month in range(1,13): # ← range represents numbered months in a year from 1 to 12
        if datetime.datetime(year,month,13).weekday() == 4: # ← day 4 from weekday() is a Friday
            friday_13ths += 1
    return friday_13ths

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
