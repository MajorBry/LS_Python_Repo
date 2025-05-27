def string_to_integer(string):
    ORD_NUM_DICT = {48: 0,
                    49: 1,
                    50: 2,
                    51: 3,
                    52: 4,
                    53: 5,
                    54: 6,
                    55: 7,
                    56: 8,
                    57: 9,}
    reversed_digits_list = [ORD_NUM_DICT[ord(char)] for char in string[::-1]]

    number = 0
    for exponent, digit in enumerate(reversed_digits_list):
        number += digit * 10**exponent
    return number

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

