"""
Problem:  create a function that converts an angle in degrees to an angle in degrees, minutes, and seconds.
    Input:  float, angle between 0 and 360 degrees
    Output:  string, angle with °, ', and "
    Rules
        Implicit:
            - (?)round to nearest second
            - (?)input float may be 0, 360, or anywhere in between
            - (?)input float is non-negative

Examples/ Test Cases:
    # All of these examples should print True
    print(dms(30) == "30°00'00\"")
    print(dms(76.73) == "76°43'48\"")
    print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
    print(dms(93.034773) == "93°02'05\"")
    print(dms(0) == "0°00'00\"")
    print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

Data Structures: skip

Algorithm
    - Set degree variable to whole part of float
    - Set degree_decimal variable to the remainder of float / 1
    - Set minute variable to whole part of (60 * degree_decimal)
    - Set minute_decimal variable to the remainder of (60 * degree_decimal) < 1
    - Set second variable to whole part of (60 * decimal)

    OR

    - convert float number to seconds
    - use remainder of number / 60 to find seconds
    - use remainder of (whole part of number / 60) / 60 to find minutes
    - use whole part of (whole part of number / 60) / 60 to find degrees

    
Code
    -Use constant variable for conversion factor of 60.
    -Use DEGREE = "\u00B0" for ° symbol.
"""
DEGREE_CHAR = "\u00B0"
CONVERSION_FACTOR = 60 # ← 60 seconds / minute and 60 minutes / degree
TOTAL_DEGREES = 360

def dms(number):
    conditioned_number = number % TOTAL_DEGREES

    total_in_seconds = conditioned_number * CONVERSION_FACTOR**2
    whole_minutes, seconds = divmod(total_in_seconds, CONVERSION_FACTOR)
    degrees, minutes = divmod(whole_minutes, CONVERSION_FACTOR)
    return f"{degrees:0.0f}{DEGREE_CHAR}{0 if minutes < 10 else ''}{minutes:0.0f}'{0 if seconds < 10 else ''}{round(seconds):0.0f}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
print(dms(-1) == "359°00'00\"")
print(dms(400) == "40°00'00\"")
print(dms(-40) == "320°00'00\"")
print(dms(-420) == "300°00'00\"")