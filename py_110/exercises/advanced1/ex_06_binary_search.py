def binary_search(search_list, term):
    half_index = len(search_list) // 2
    center_term = search_list[half_index]
    
    if center_term == term:
        return half_index
    elif half_index == 0:
        return -1
    elif center_term < term:
        result = binary_search(search_list[half_index:], term)
        if result == -1:
            return -1
        return half_index + result
    else:
        result = binary_search(search_list[:half_index], term)
        if result == -1:
            return -1
        return result
    
# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)
names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)

