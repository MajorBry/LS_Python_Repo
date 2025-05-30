lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def select_multiples_of_three(list_):
    return [element for element in list_ if element % 3 == 0]

new_lst = [select_multiples_of_three(sublist) for sublist in lst]
print(lst)
print(new_lst)