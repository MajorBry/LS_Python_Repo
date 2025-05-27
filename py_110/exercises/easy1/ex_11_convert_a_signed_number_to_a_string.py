def integer_to_string(integer):
    BASE = 10
    INT_STR_DICT = {0: '0',
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                    6: '6',
                    7: '7',
                    8: '8',
                    9: '9',}
    
    chars = []
    while integer: # ← condition checks whether there are more digits to process
        chars.insert(0, INT_STR_DICT[integer % BASE])
        integer //= BASE

    return ''.join(chars) or '0'

def signed_integer_to_string(integer):
    if integer > 0:
        return '+' + integer_to_string(integer)
    elif integer < 0:
        return '-' + integer_to_string(-integer)
    return '0'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
