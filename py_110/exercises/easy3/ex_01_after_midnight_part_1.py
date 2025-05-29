"""
Problem:  write a function named time_of_day that converts time of day in minutes before or after midnight and converts that to time of day in HH:MM format
    Input:  integer, positive or negative minutes
    Output:  string, "00:00" ("HH:MM") format
    Rules
        Explicit
            - may not use datetime module
            - input could be any integer, including 0
            - disregard daylight savings / standard time complications
        Implicit
            - 
    Questions
        - 

Examples/ Test Cases
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

Data Structures:  

Algorithm
    - change input minutes to a condition minutes value: corresponding to a 1-day cycle
    
    - set hours as quotient of conditioned minutes divided by number of minutes in an hour
    - set minutes as remainder of conditioned minutes divided by number of minutes in an hour

    - format return string so a 0 is added before hours and/or minutes if their values are < 10, respectively
    - return formatted HH:MM string


Implementation by Code
    - Note: there are 1440 minutes in a day
    - Use modulo operator (%) to get negative and positive minutes into minutes within the 24-hour cycle (i.e. minutes % 1440)
    - Use tuple unpacking with divmod to set hours and minutes
"""
def time_of_day(minutes):
    MINUTES_IN_A_DAY = 1440
    MINUTES_IN_AN_HOUR = 60

    def condition_minutes(minutes):
        return minutes % MINUTES_IN_A_DAY
    
    def hhmm_string(hours, minutes):
        return f"{hours:02d}:{minutes:02d}"

    minutes = condition_minutes(minutes)
    hh_hours, mm_minutes = divmod(minutes, MINUTES_IN_AN_HOUR)
    return hhmm_string(hh_hours, mm_minutes)

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
