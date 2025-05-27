numbers = []
numbers.append(int(input('Enter the 1st number: ')))
numbers.append(int(input('Enter the 2nd number: ')))
numbers.append(int(input('Enter the 3rd number: ')))
numbers.append(int(input('Enter the 4th number: ')))
numbers.append(int(input('Enter the 5th number: ')))
last_number = int(input('Enter the last number: '))

if last_number > max(numbers):
    print(f'{last_number} is greater than any one of {', '.join([str(number) for number in numbers])}.')
else:
    print(f"{last_number} isn't greater than all of {', '.join([str(number) for number in numbers])}.")

# numbers.append(input('Enter the 1st number: '))
# numbers.append(input('Enter the 2nd number: '))
# numbers.append(input('Enter the 3rd number: '))
# numbers.append(input('Enter the 4th number: '))
# numbers.append(input('Enter the 5th number: '))
# last_number = input('Enter the last number: ')

# if last_number in numbers:
#     print(f'{last_number} is in {','.join(numbers)}.')
# else:
#     print(f"{last_number} isn't in {','.join(numbers)}.")
