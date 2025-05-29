def repeater(string):
    double_char_list = []
    for char in string:
        double_char_list.append(char*2)
    return ''.join(double_char_list)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
