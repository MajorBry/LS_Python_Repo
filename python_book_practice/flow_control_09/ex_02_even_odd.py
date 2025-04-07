# ↓ number is assumed to always be an integer.
def is_even(number):
    return True if (number % 2) == 0 else False

def even_or_odd(number):
    print('even' if is_even(number) else 'odd')

even_or_odd(2)
even_or_odd(3)