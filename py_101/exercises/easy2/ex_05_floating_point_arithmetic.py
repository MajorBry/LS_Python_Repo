def prompt(text):
    print(f'==> {text}')

prompt('Enter the first number:')
num1 = float(input())
prompt('Enter the second number:')
num2 = float(input())

prompt(f'{num1} + {num2} = {num1 + num2}')
prompt(f'{num1} - {num2} = {num1 - num2}')
prompt(f'{num1} * {num2} = {num1 * num2}')
prompt(f'{num1} / {num2} = {num1 / num2}')
prompt(f'{num1} // {num2} = {num1 // num2}')
prompt(f'{num1} % {num2} = {num1 % num2}')
prompt(f'{num1} ** {num2} = {num1**num2}')