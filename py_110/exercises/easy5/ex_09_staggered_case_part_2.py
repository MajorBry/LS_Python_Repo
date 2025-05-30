def staggered_case(string):
    change_case = True
    string_list = []

    for char in string:
        if char.isalpha():
            if change_case:
                string_list.append(char.upper())
            else:
                string_list.append(char.lower())
            change_case = not change_case
        else:
            string_list.append(char)

    return ''.join(string_list)

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True