"""
Problem:  create multiplicative_average function
    input:  list of positive integers
    output:  string (value rounded to 3 decimal points)

E/T
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

Algorithm
    - set product = 1
    - iterate over numbers_list: product *= integer (product will still be of type integer)
    - set average = product / len(numbers_list)
    - return formatted string f'{average:.3f}'
    
Code:
    - format of string is of the form f'{number:.3f}'
"""
def multiplicative_average(numbers_list):
    product = 1
    
    for number in numbers_list:
        product *= number
    average = product / len(numbers_list)
    return f'{average:.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
