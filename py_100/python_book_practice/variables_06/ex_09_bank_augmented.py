# 	8. Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.
# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.
# Use augmented assignment to compute the final result, one year at a time.

P = 1000.00 # ← Initial amount in bank.
APR = .05
i = 1.05
years = 5 # ← Time elapsed since initial investment

i **= years # ← Interest multiplier after «years» years
balance = P*i # ← The balance after «years» years
print(f'After {years} years, the balance of you bank account will be ${balance:,.2f}.')

# balance = 1000
# balance *= 1.05
# balance *= 1.05
# balance *= 1.05
# balance *= 1.05
# balance *= 1.05
# print(balance)