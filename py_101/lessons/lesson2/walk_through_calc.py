# Welcome user and ask for input.
print('Welcome to Calculator!')
num1 = int(input("What's the first number?  "))
num2 = int(input("What's the second number?  "))
operation = input('What operation would you like to perform?\n1) Add 2) Subtract 3) Multipy 4) Divide\n')

# Perform operation
match operation:
    case '1':
        output = num1 + num2
    case '2':
        output = num1 - num2
    case '3':
        output = num1 * num2
    case '4':
        output = num1 / num2
    case _:
        print('Error')

# Print result
print(f'The result is: {output}')