dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def color_descriptor(colors):
    return [color.capitalize() for color in colors]

produce_descriptors = []
# if type fruit return colors
# if type vegetable return size

for subdict in dict1.values():
    if subdict['type'] == 'fruit':
        produce_descriptors.append(color_descriptor(subdict['colors']))
    elif subdict['type'] == 'vegetable':
        produce_descriptors.append(subdict['size'].upper())

produce_descriptors2 = [color_descriptor(subdict['colors']) if subdict['type'] == 'fruit' else subdict['size'].upper() for subdict in dict1.values()]


print(produce_descriptors)
print(produce_descriptors2)