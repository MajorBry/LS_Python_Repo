# ↓ Assume list with element lists. list1 and list2 are duplicates (copies) of each other.
def list_id_comparison(list1,list2):
    for x in range(0,len(list1)):
        for y in range(0,len(list1[x])):
            print(id(list1[x][y]) == id(list2[x][y]))

my_list = [[1, 2, 3], [4, 5, 6]]
another_list = list(my_list)

list_id_comparison(my_list,another_list)

print(id(my_list) == id(another_list))

# print(my_list,another_list,sep = '\n')
# my_list += [[7,8,9]]
# print(my_list,another_list,sep = '\n')