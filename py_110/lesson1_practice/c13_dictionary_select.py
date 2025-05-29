def select_fruit(fruit_dict):
    return {ind:el for ind, el in fruit_dict.items() if el == 'Fruit'}

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }
