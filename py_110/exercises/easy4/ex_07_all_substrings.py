def leading_substrings(string):
    return [string[0:i] for i in range(1,len(string) + 1)]

def substrings(string):
    string_list = []
    for i in range(len(string)):
        string_list.extend(leading_substrings(string[i:]))
    return string_list

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
print(substrings('abcde') == expected_result)  # True