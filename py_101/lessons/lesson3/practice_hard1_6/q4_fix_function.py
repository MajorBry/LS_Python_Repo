def is_an_ip_number(string):
    try:
        int(string)
    except:
        return False
    return int(string) in range(0,256)

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    if len(dot_separated_words) != 4: # ← added
        return False  # ← added

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False  # ← changed from: break

    return True

print(is_dot_separated_ip_address('1.2.3.4'))