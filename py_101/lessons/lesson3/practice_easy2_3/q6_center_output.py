MAX_DISPLAY_CHAR = 40 # Width of table

title = "Flintstone Family Members"
text_width = len(title)
left_buffer_width = (MAX_DISPLAY_CHAR - text_width) // 2
right_buffer_width = (MAX_DISPLAY_CHAR - text_width) - left_buffer_width

buffered_title = ' '*left_buffer_width + title + ' '*right_buffer_width

print('-'*MAX_DISPLAY_CHAR)
print(buffered_title)
print(title.center(MAX_DISPLAY_CHAR)) # ← Built-in method for doing the same thing.
print('-'*MAX_DISPLAY_CHAR)