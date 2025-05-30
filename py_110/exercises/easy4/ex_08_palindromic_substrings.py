def leading_substrings(string):
    return [string[0:i] for i in range(1,len(string) + 1)]

def substrings(string):
    string_list = []
    for i in range(len(string)):
        string_list.extend(leading_substrings(string[i:]))
    return string_list

def is_palindrome(string):
    return bool(string == ''.join(reversed(string)) and len(string) > 1)

def palindromes(string):
    return [substring for substring in substrings(string) if is_palindrome(substring)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True
print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True
print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True
