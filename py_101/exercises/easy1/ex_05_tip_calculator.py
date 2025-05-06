bill = float(input('How much was your bill?: $'))
print('What tip do you want to give (e.g. insert \'15\' for 15%)?')
rate = float(input())

tip = round(bill * rate / 100, ndigits=2)
total = tip + bill
print(f'Your tip is ${tip} and your final bill amounts to ${total}.')