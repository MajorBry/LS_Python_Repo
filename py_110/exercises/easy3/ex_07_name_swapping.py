def swap_name(full_name):
    name_parts = full_name.split(' ')
    return f'{name_parts.pop()}, {' '.join(name_parts)}'


print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True