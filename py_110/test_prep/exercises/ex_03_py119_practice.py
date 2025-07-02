"""
Problem:  Create a function that converts every second character in every third word to uppercase.
    Input:  string
    Output:  string, uppercase transformation of input string
    Rules
        Explicit
            - capitalize every other character (starting with the second character) of every 3rd word
        Implicit
            - lowercase letters and uppercase letters in the original word
            - (?)characters other than transformed lower-to-upper-case letters remain the same
            - words are space-delimited 
    Questions
        - ()

Examples/ Test Cases
↓↓

Data Structures:  change each word to list, to more easily capitalize each 2nd letter of every 3rd word

Algorithm
    - create a list of 'words', delimited by whitespace characters
    - iterate over list elements, capitalizing every 2nd letter of every 3rd word
        + capitalize every 2nd letter: 
            1) iterate over every character, replacing each 2nd letter with it's capitalized version

Implementation by Code
    - str.split() default delimiter is whitespace
    - str.upper() returns any non-letter characters in the string as-is
"""
def capitalize_nth_letter(word, n):
    transformed_chars = [char.upper() if (index + 1) % n == 0 else char for index, char in enumerate(word)]
    return ''.join(transformed_chars)

def to_weird_case(string):
    n_word = 3 # ← process every n_word from list
    n_char = 2 # ← capitalize every n_char character
    delimiter = ' '
    
    words = string.split(delimiter)
    for index, word in enumerate(words):
        if (index + 1) % n_word == 0:
            words[index] = capitalize_nth_letter(word, n_char)
        else:
            words[index] = word
    
    return delimiter.join(words)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)
original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)
print(to_weird_case('aaA bB c') == 'aaA bB c')
original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
