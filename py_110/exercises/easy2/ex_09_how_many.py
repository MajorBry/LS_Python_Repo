def print_occurrences(dictionary):
    for key, value in dictionary.items():
        print(f'{key} => {value}')

def count_occurrences(lst):
    occurrences_dict = {}
    for element in lst:
        occurrences_dict[element.casefold()] = occurrences_dict.get(element.casefold(), 0) + 1
    print_occurrences(occurrences_dict)

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']
count_occurrences(vehicles)