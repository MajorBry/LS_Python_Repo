def short_long_short(s1, s2):
    if len(s1) > len(s2):
        return s2 + s1 + s2
    else:
        return s1 + s2 + s1

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")