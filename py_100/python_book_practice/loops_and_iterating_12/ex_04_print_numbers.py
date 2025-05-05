my_list = [6, 3, 0, 11, 20, 4, 17]

# ↓ Even Values
i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        print(my_list[i])
    i += 1

# ↓ Odd Values
for num in my_list:
    if num % 2 != 0:
        print(num)


