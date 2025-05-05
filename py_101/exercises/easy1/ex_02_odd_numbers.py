# # Solution
# numbers = range(1,100,2)
# for number in numbers:
#     print(number)
def is_odd(num):
    return not abs(num) % 2 == 0

def invalid_number(num):
    try:
        int(num)
    except ValueError:
        print('Invalid number.')
        return True
    return False

def odd_numbers(start, end):
    if is_odd(start):
        numbers = range(start, end + 1, 2)
    else:
        numbers = range(start + 1, end + 1, 2)

    for number in numbers:
        print(number)

num1 = input('Starting Integer: ')
while invalid_number(num1):
    num1 = input('Starting Integer: ')

num2 = input('Ending Integer: ')
while invalid_number(num2):
    num2 = input('Ending Integer: ')

odd_numbers(int(num1), int(num2))