def unique_sequence(int_sequence):
    return [int_sequence[i] for i in range(len(int_sequence)) if i == 0 or int_sequence[i] != int_sequence[i - 1]]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True