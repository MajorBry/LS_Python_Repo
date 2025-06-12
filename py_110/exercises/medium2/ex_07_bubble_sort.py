def bubble_sort(lst):
    sorting = True

    while sorting:
        sorting = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst.insert(i, lst.pop(i + 1))
                sorting = True
            
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True
lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True
lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)
expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True
