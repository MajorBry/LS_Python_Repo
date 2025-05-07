def center_of(string):
    if string:
        if len(string) % 2 == 0:
            half_length = len(string) // 2
            return string[(half_length - 1):(half_length) + 1]
        else:
            middle_index = len(string) // 2 # ← integer division gives the correct index of middle number.
            return string[middle_index]
        
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
