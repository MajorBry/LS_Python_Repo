def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

numbers1 = [0,1,2,3,4,5]
numbers2 = [0,1,2,3,4,5]
number = 6
add_to_rolling_buffer1(numbers1, 6, 6)
add_to_rolling_buffer2(numbers2, 6, 6)

print(numbers1)
print(numbers2)