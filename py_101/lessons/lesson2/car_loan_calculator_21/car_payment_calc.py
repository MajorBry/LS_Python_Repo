def prompt(message):
    print(f'==> {message}')

def invalid_float_str(number):
    try:
        float(number)
    except ValueError:
        return True
    if float(number) <= 0:
        return True
    return False

def invalid_int_str(number):
    try:
        int(number)
    except ValueError:
        return True
    if int(number) <= 0:
        return True
    return False

def car_payment(defaults=None):
    # The 'defaults' variable contains either None (first run) or a dictionary with values for the last principal, apr, and months.

    # ↓ If this isn't the first iteration (default != None).
    if defaults:
        prompt('*Press "Enter" to accept current value, or input another value.')
        prompt(f'Loan amount: ${defaults['principal']}')
        principal = input()
        if principal == '':
            principal = defaults['principal']
        else:
            while invalid_float_str(principal):
                prompt('Invalid input. Must be a positive number.')
                prompt('What is the loan amount?: $')
                principal = input()

        prompt(f'Interest rate (APR): {defaults['apr']}%')
        apr = input()
        if apr == '':
            apr = defaults['apr']
        else:
            while invalid_float_str(apr):
                prompt('Invalid input. Must be a positive number.')
                prompt('What is the interest rate (APR)?: %')
                apr = input()

        prompt(f'Loan duration: {defaults['months']} months')
        months = input()
        if months == '':
            months = defaults['months']
        else:
            while invalid_int_str(months):
                prompt('Invalid input. Must be a positive integer.')
                prompt('What is the loan duration (months)?: ')
                months = input()
    # ↓ This is used for the first iteration.
    else:
        prompt('What is the loan amount?: $')
        principal = input()
        while invalid_float_str(principal):
            prompt('Invalid input. Must be a positive number.')
            principal = input()

        prompt('What is the interest rate (APR)?: %')
        apr = input()
        while invalid_float_str(apr):
            prompt('Invalid input. Must be a positive number.')
            apr = input()

        prompt('What is the loan duration (months)?: ')
        months = input()
        while invalid_int_str(months):
            prompt('Invalid input. Must be a positive integer.')
            months = input()

    # ↓ Monthly Percentage Rate (MPR)
    mpr = float(apr) / 12

    # ↓ Monthly Payment
    payment = round(float(principal) * (mpr/100 / (1 - (1 + mpr/100)**(-int(months)))), ndigits=2)

    # Print result
    prompt(f'Your monthly payment is ${payment:.2f}')

    return({'principal':principal, 'apr':apr, 'months':months})

# Welcome user and ask for input.
prompt('Welcome to the Monthly Car Payment Calculator!')

decision = 'yes'
default_vals = None
# ↓ Loop to run the payment calculator as many times as the user wants.  Uses values from previous iteration, unless overridden by user input.
while decision.casefold() in ['yes', 'yeah', 'y']:
    default_vals = car_payment(default_vals)
    prompt('Would you like to perform another car payment calculation?')
    decision = input()