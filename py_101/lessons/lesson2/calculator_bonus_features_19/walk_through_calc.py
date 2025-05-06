import json

LANGUAGE = 'en'

# Open the JSON file for reading
with open('/home/bry/my_linux_files/LS_Python_Repo/py_101/lessons/lesson2/calculator_bonus_features_19/calc_messages.json', 'r') as file:
    msg = json.load(file)[LANGUAGE]

def prompt(message):
    print(f'==> {message}')

def invalid_number(number):
    try:
        float(number)
    except ValueError:
        return True
    return False

def calc():
    prompt(msg["1st number"])
    num1 = input()
    while invalid_number(num1):
        prompt(msg["invalid"])
        num1 = input()

    prompt(msg["2nd number"])
    num2 = input()
    while invalid_number(num2):
        prompt(msg["invalid"])
        num2 = input()

    prompt(msg["what operation"])
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(msg["choose 1, 2, 3, 4"])
        operation = input()

    # Perform operation
    match operation:
        case '1':
            output = float(num1) + float(num2)
        case '2':
            output = float(num1) - float(num2)
        case '3':
            output = float(num1) * float(num2)
        case '4':
            output = float(num1) / float(num2)
        case _:
            prompt('Error')

    # Print result
    prompt(f'{msg["result is"]}{output}')

# Welcome user and ask for input.
prompt(msg["welcome"])

decision = 'yes'
while decision.casefold() in msg['yes_list']:
    calc()
    prompt(msg["again?"])
    decision = input()