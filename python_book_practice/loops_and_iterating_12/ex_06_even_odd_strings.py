my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# All numbers in my_list are integers, therefore result of num % 2 is always 1 or 0, 'odd' or 'even'.
even_odd = ('even', 'odd')
string_list = [even_odd[num % 2] for num in my_list]
print(string_list)

# ↓ Or, using a ternary expression:
print(['even' if num % 2 == 0 else 'odd' for num in my_list])