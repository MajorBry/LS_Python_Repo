data_set = {1, 2, 3, 4, 5}

even_items = set()
for item in data_set:
    if item % 2 == 0:
        even_items.add(item)

for item in even_items:
    data_set.remove(item)

print(data_set)