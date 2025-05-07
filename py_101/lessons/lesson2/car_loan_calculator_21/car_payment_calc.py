MESSAGES = {
    'press enter': '*Press "Enter" to accept current value, or input another value.',
    'amount': 'Loan amount: $',
    'invalid float': 'Invalid input. Must be a positive number.',
    'amount?': 'What is the loan amount?: $',
    'rate': 'Interest rate (APR):',
    'rate?': 'What is the interest rate (APR)?: %',
    'duration': 'Loan duration:',
    'invalid integer': 'Invalid input. Must be a positive integer.',
    'duration?': 'What is the loan duration (months)?:',
    'duration units': 'months',
    'payment is': 'Your monthly payment is ',
    'welcome': 'Welcome to the Monthly Car Payment Calculator!',
    'decision': 'yes',
    'decision list': ['yes', 'yeah', 'y'],
    'again?': 'Would you like to perform another car payment calculation?',
}

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str, convert_func=float):
    try:
        convert_func(number_str)
    except ValueError:
        return True
    if convert_func(number_str) <= 0:
        return True
    return False

def get_next_iteration_input(value, value_type):
    match value_type:
        case 'amount':
            prompt(f'{MESSAGES['amount']}{value}')
            msg1 = 'invalid float'
            msg2 = 'amount?'
        case 'rate':
            prompt(f'{MESSAGES['rate']} {value}%')
            msg1 = 'invalid float'
            msg2 = 'rate?'
        case 'duration':
            prompt(f'{MESSAGES['duration']} {value} {MESSAGES['duration units']}')
            msg1 = 'invalid integer'
            msg2 = 'duration?'
        case _:
            return None
    
    result = input()
    if result == '':
        return value
    else:
        while invalid_number(result):
            prompt(MESSAGES[msg1])
            prompt(MESSAGES[msg2])
            result = input()
    return result

def car_payment(defaults=None):
    # The 'defaults' variable contains either None (first run) or a dictionary with values for the last principal, apr, and months.

    # ↓ If this isn't the first iteration (default != None).
    if defaults:
        prompt(MESSAGES['press enter'])
        principal = get_next_iteration_input(defaults['principal'], 'amount')
        apr = get_next_iteration_input(defaults['apr'], 'rate')
        months = get_next_iteration_input(defaults['months'], 'duration')
    # ↓ This is used for the first iteration.
    else:
        prompt(MESSAGES['amount?'])
        principal = input()
        while invalid_number(principal):
            prompt(MESSAGES['invalid float'])
            principal = input()

        prompt(MESSAGES['rate?'])
        apr = input()
        while invalid_number(apr):
            prompt(MESSAGES['invalid float'])
            apr = input()

        prompt(MESSAGES['duration?'])
        months = input()
        while invalid_number(months, int):
            prompt(MESSAGES['invalid integer'])
            months = input()

    # ↓ Monthly Percentage Rate (MPR)
    mpr = float(apr) / 12

    # m = p * (j / (1 - (1 + j) ** (-n)))
	# 
    # m = monthly payment
	# p = loan amount
	# j = monthly interest rate
    # n = loan duration in months
    # 
    # ↓ Monthly Payment
    payment = round(float(principal) * (mpr/100 / (1 - (1 + mpr/100)**(-int(months)))), ndigits=2)

    # Print result
    prompt(f'{MESSAGES['payment is']}{payment:.2f}')

    return({'principal':principal, 'apr':apr, 'months':months})

# Welcome user and ask for input.
prompt(MESSAGES['welcome'])

decision = MESSAGES['decision']
default_vals = None
# ↓ Loop to run the payment calculator as many times as the user wants.  Uses values from previous iteration, unless overridden by user input.
while decision.casefold() in MESSAGES['decision list']:
    default_vals = car_payment(default_vals)
    prompt(MESSAGES['again?'])
    decision = input()
