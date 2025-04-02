my_dict = {
    'dog': 'barks',
    'cat': 'purrs',
    'pig': 'oinks',
}

# print(my_dict['cat'])
# print(type(my_dict['cat']))

my_dict['cat'] = {'says': 'meow',
                  'sleeps': 'at night',
                  'eats':'fish',
                  }

#print(my_dict['cat'])
#print(type(my_dict['cat']))
print(my_dict['cat']['says'])