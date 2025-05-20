MONTHS = {
    1: 'JaNuArY',
    2: 'february',
    3: 'MaRch',
    4: 'ApriL',
    5: 'mAY',
    6: 'jUne',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'oCTOber',
    11: 'november',
    12: 'deCember'
}

month_names = MONTHS.values()

def cap_values(d):
    for key, value in d.items():
        d[key] = value.capitalize()

    return d

capitalized_months = cap_values(MONTHS)
print(list(month_names))
# ['January', 'February', 'March', 'April',
#   'May', 'June', 'July', 'August', 'September',
#   'October', 'November', 'December']