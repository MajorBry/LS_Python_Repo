"""
Problem:  write 2 functions, after_midnight() and before_midnight()
    Input:  string (both), of format 'HH:MM'
    Output:  integer (both), of minutes after and before midnight, respectively
    Rules
        Explicit
            - return value (both) may be anywhere between 0 and 1439
        Implicit
            - 0 (both) is returned for both '00:00' and '24:00'
    Questions
        - 

Examples/ Test Cases
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

Data Structures:  

Algorithm
    - 

Implementation by Code
    minutes = [int(hours)*60 + int(minutes) for hours, minutes in time_string.split(':')][0]
    
    if minutes in range(1, 1440):
        return minutes
    else:
        return 0
"""
MINUTES_IN_DAY = 1440
MINUTES_IN_HOUR = 60

def after_midnight(time_string):
    hours, minutes = time_string.split(':')
    sum_minutes = int(hours) * MINUTES_IN_HOUR + int(minutes)
    
    if sum_minutes in range(1, MINUTES_IN_DAY):
        return sum_minutes
    else:
        return 0
    
def before_midnight(time_string):
    after_midnight_minutes = after_midnight(time_string)
    if after_midnight_minutes:
        return MINUTES_IN_DAY - after_midnight_minutes
    else:
        return 0
    

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
