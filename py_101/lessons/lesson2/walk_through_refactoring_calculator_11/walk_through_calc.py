def prompt(message):
    print(f'==> {message}')

def invalid_number(number):
    try:
        int(number)
    except ValueError:
        return True
    return False

# Welcome user and ask for input.
prompt('Welcome to Calculator!')

prompt("What's the first number?")
num1 = input()
while invalid_number(num1):
    prompt('Invalid number.')
    num1 = input()

prompt("What's the second number?  ")
num2 = input()
while invalid_number(num2):
    prompt('Invalid number.')
    num2 = input()

prompt('''What operation would you like to perform?
       1) Add 2) Subtract 3) Multipy 4) Divide''')
operation = input()
while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

# Perform operation
match operation:
    case '1':
        output = int(num1) + int(num2)
    case '2':
        output = int(num1) - int(num2)
    case '3':
        output = int(num1) * int(num2)
    case '4':
        output = int(num1) / int(num2)
    case _:
        prompt('Error')

# Print result
prompt(f'The result is: {output}')