# Assume input string will always contain at least 2 words.
def penultimate(text):
    words = text.split()
    return words[-2]

def middle(text):
    words = text.split()
    if len(words) % 2 == 1:
        return words[(len(words) - 1) // 2]
    else:
        return None

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

print(middle("last word") == None)
print(middle("Launch School is great!") == None)
print(middle('one more time') == 'more')
print(middle('hi') == 'hi')
print(middle('') == None)