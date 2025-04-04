# Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now.
age = int(input('How old are you? '))
print(f'You are {age} years old.')
for t in range(10,50,10):
    print(f'In {t} years, you will be {age + t} years old.')
