lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odd(numbers):
    return sum([num for num in numbers if num % 2 == 1])

new_list = sorted(lst, key=sum_odd)
print(new_list)
print(lst)