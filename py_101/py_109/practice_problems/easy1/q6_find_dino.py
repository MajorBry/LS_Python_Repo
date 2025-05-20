def include_dino(string):
    print(True if string.find('Dino') > 0 else False)

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

include_dino(str1)
include_dino(str2)