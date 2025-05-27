def word_sizes(string):
    # ↓ Reassigns local variable `string` to a filtered version of string (removing any non-letters/non-spaces).
    string = ''.join([char for char in string if char.isalpha() or char.isspace()])
    
    if not string:
        return {}

    word_size_dictionary = {}
    string_list = string.split(' ')
    
    while string_list:
        if len(string_list[0]) in word_size_dictionary:
            word_size_dictionary[len(string_list.pop(0))] += 1
        else:
            word_size_dictionary[len(string_list.pop(0))] = 1
    return word_size_dictionary

# All of these examples should print True
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})
string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})
string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})
string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})
print(word_sizes('') == {})