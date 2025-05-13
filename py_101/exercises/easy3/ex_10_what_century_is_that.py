def century(year):
    SUFFIX = {
                  '01': 'st',
                  '1': 'st',
                  '21': 'st',
                  '31': 'st',
                  '41': 'st',
                  '51': 'st',
                  '61': 'st',
                  '71': 'st',
                  '81': 'st',
                  '91': 'st',
                  '02': 'nd',
                  '2': 'nd',
                  '22': 'nd',
                  '32': 'nd',
                  '42': 'nd',
                  '52': 'nd',
                  '62': 'nd',
                  '72': 'nd',
                  '82': 'nd',
                  '92': 'nd',
                  '03': 'rd',
                  '3': 'rd',
                  '23': 'rd',
                  '33': 'rd',
                  '43': 'rd',
                  '53': 'rd',
                  '63': 'rd',
                  '73': 'rd',
                  '83': 'rd',
                  '93': 'rd',
                  }
    century_integer = year // 100
    century_remainder = year % 100
    if century_remainder == 0:
        century_year = str(century_integer)
    else:
        century_year = str(century_integer + 1)
    return century_year + (SUFFIX[century_year[-2:]] if century_year[-2:] in SUFFIX else 'th')

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
