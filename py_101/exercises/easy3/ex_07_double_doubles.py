def twice(num):
    num_as_string = str(num)
    if len(num_as_string) % 2 == 0:
        left_digits = num_as_string[:(len(num_as_string) // 2)]
        right_digits = num_as_string[(len(num_as_string) // 2):]
        if left_digits == right_digits:
            return num
    return num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
