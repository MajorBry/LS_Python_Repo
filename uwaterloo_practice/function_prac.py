# def square(x):
#     return x*x
#
# print(square(10))
# print(square(square(2)))

def lowerChar(char):
    char_n = ord(char)
    if char_n >= 65 and char_n <= 90:
        char_n += 32
        return chr(char_n)
    else:
        return char

def lowerString(string):
    result = ''
    for i in string:
        result += lowerChar(i)
    return result

print(lowerString('This string has 9 CAPITAL letters (& Punctuation)!'))