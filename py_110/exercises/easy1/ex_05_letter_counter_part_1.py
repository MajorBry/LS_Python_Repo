def word_sizes(string):
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

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})
string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})
string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})
string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})
print(word_sizes('') == {})