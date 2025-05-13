def ends_with_exclamation(text):
    return text.endswith('!')

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(ends_with_exclamation(str1))
print(ends_with_exclamation(str2))