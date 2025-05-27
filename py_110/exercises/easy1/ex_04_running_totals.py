def running_total(numbers):
    if numbers:
        new_numbers = [numbers[0]]
        for number in numbers[1:]:
            new_numbers.append(number + new_numbers[-1])
        return new_numbers
    else:
        return numbers

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
