def ascii_art(text, x=10):
    for i in range(1, x + 1):
        print('-'*i + text)

ascii_art('The Flintstones Rock!', 10)