def crunch(string):
    if len(string) > 1:
        string_list = [string[0]]
        for i in range(1,len(string)):
            if string[i] != string_list[-1]:
                string_list.append(string[i])
        return ''.join(string_list)
    return string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
