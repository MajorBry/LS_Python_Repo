def find_greatest(numbers):
    if numbers is None:
        return

    iterator = 0
    saved_number = numbers[iterator]
    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number
        iterator += 1
    return saved_number

print(find_greatest([1,5,9,10,30,6,8]))
print(find_greatest(None))