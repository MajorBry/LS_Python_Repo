def clean_up(text):
    char_list = [(char if char.isalpha() else ' ') for char in text]
    alpha_text = ''.join(char_list)
    while alpha_text != alpha_text.replace('  ', ' '):
        alpha_text = alpha_text.replace('  ', ' ')
    return alpha_text

print(clean_up("---what's my +*& line?") == " what s my line ")