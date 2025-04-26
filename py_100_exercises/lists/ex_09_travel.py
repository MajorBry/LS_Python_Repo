destinations =['Prague','London','Sydney','Belfast','Rome','Aruba','Paris','Bora Bora','Barcelona','Rio de Janeiro','Marrakesh','New York City']

def included(element, list):
    # Option 1
    number_of_matches = len([item for item in list if item == element])
    return (True if number_of_matches else False)

    # # Option 2
    # i = 0
    # while i < len(list):
    #     if list[i] == element:
    #         return True
    #     i += 1
    # return False

print(included('Barcelona',destinations)) # True
print(included('Nashville',destinations)) # False
