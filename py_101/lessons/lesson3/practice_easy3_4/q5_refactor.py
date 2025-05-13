def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
def is_color_valid1(color):
    return bool(color == "blue" or color == "green")

def is_color_valid2(color):
    return True if color == "blue" or color == "green" else False

print(is_color_valid('blue'), is_color_valid1('blue'), is_color_valid2('blue'))

print(is_color_valid('green'), is_color_valid1('green'), is_color_valid2('green'))

print(is_color_valid('red'), is_color_valid1('red'), is_color_valid2('red'))