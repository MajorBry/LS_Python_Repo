def invalid_number(num):
    try:
        int(num)
    except ValueError:
        print('Invalid number.')
        return True
    if int(num) <= 0:
        return True
    return False

num = input('Please enter an integer greater than 0: ')
while invalid_number(num):
    num = input('Please enter an integer greater than 0: ')

operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')
while operation not in ('s', 'p'):
    print('Invalid input.')
    operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')

if operation == 's':
    operation = 'sum'
    result = sum(range(1, int(num) + 1))
else:
    operation = 'product'
    result = 1
    for multiplicand in range(1, int(num) + 1):
        result *= multiplicand

print(f'The {operation} of the integers between 1 and {int(num)} is: {result}')