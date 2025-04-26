def is_empty_or_blank(s):
    return is_empty(s) or s.isspace()

def is_empty(string):
    return not(len(string))

print(is_empty_or_blank('mars'))# False
print(is_empty_or_blank('  '))# True
print(is_empty_or_blank(''))# True