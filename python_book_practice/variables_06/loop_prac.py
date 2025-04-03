list2 = ['banana', 'apple', 'grape']
list2 += 'orange'  # ← Oops, accidentally added 'orange' as a string set (rather than as a list element).

# ↓ Loop to delete single-character strings.
i = 0
while i < len(list2): # ← Using while-loop with variable incrementation since index will change as items are deleted, so a new list element will occupy the same space
    if len(list2[i]) == 1:
        del list2[i]
    else:
        i += 1 # ← Variable incrementation due to else statement
print(list2)