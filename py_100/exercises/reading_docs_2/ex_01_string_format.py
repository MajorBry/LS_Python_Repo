name = "Victor"
profession = "programmer"
# 1. How can you print the string Hello, Victor. You are a programmer. using the str.format method? You should fill in the name and profession in a string literal that contains the rest of the text.
print("Hello, {0}. You are a {1}.".format(name, profession))

# 2. How can you achieve the same result using an f-string?
print(f'Hello, {name}. You are a {profession}.')

