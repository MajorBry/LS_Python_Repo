import random

def new_char():
    # Code points for 'a' through 'f' are 97 - 102
    field_num = random.randint(0, 15)
    if field_num > 9:
        return chr(87 + field_num)
    return str(field_num)

def uuid():
    uuid_sections = [8, 4, 4, 4, 12]
    
    return '-'.join([''.join([new_char() for num in range(section_length)]) for section_length in uuid_sections])

print(uuid())

# ↓ Test to see if many of these calls will remain collision-free
test_iterations = 100000
print(len({uuid() for num in range(test_iterations)}) == test_iterations)