def stringy(num):
    string_list = []
    for index in range(num):
        string_list.append('1') if index % 2 == 0 else string_list.append('0')
    return ''.join(string_list)

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
