def swap(string):
    words_list = string.split()

    for index, word in enumerate(words_list):
        if len(word) > 1:
            word = word[-1] + word[1:-1] + word[0]
            words_list[index] = word
    return ' '.join(words_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
