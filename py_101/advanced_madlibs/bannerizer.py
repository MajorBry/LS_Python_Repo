MIN_PADDING = 2
MAX_WIDTH = 80 # ← Max width of box on screen
BORDER_THICKNESS = 1 # ← how thick the boarder is
# ↓ DL: DRAWING_LINES
DL = ('\u250c', #0 '┌'
                 '\u2518', #1 '┘'
                 '\u2514', #2 '└'
                 '\u2510', #3 '┐'
                 '\u2502', #4 '│'
                 '\u2500') #5 '─'

# ↓ width (int), border (int)
# width: represents width of entire box, including border
# border: represents border thickness (usually 1)
# → returns a list of top line strings
def top_line(width, border=1):
    top_line_list = []
    for i in range(border,0,-1):
        string = DL[4]*(border - i) + DL[0] + DL[5]*(width - 2*border + 2*(i - 1)) + DL[3] + DL[4]*(border - i)
        top_line_list.append(string)
    return top_line_list

def bottom_line(width, border=1):
    bottom_line_list = []
    for i in range(1,border + 1):
        string = DL[4]*(border - i) + DL[2] + DL[5]*(width - 2*border + 2*(i - 1)) + DL[1] + DL[4]*(border - i)
        bottom_line_list.append(string)
    return bottom_line_list

def empty_line(width, border=1):
    empty_line_string = DL[4]*border + ' '*(width - 2*border) + DL[4]*border
    return empty_line_string

def wrap_index(string, width):
    if len(string) <= width:
        return width
    return (string[:width].rfind(' ') if string[:width].rfind(' ') > -1 else width)

# ↓ inner_width (integer) is the width of box - borders and - min_padding
def wrap(text, inner_width):
    wrapped_list = []
    text_list = text.split('\n')
    for string in text_list:
        if len(string) > inner_width:
            while string:
                index = wrap_index(string, inner_width)
                # if len(text) > inner_width:
                #     index = wrap_index(string, inner_width)
                # else:
                #     index = inner_width
                wrapped_list.append(string[:index + 1])
                string = string[index + 1:]
            continue
        wrapped_list.append(string)
    return wrapped_list

def text_line(text, width, border=1, min_padding=1):
    inner_width = width - 2*border - 2*min_padding

    text_list = []
    text_list.extend(wrap(text, inner_width))

    result_list = []
    for string in text_list:
        left_pad = (width - len(string) - 2*border) // 2
        right_pad = width - len(string) - 2*border - left_pad
        result_list.append(DL[4]*border + ' '*left_pad + string + ' '*right_pad + DL[4]*border)
    return result_list

def print_in_box(text, width=MAX_WIDTH, border_thickness=BORDER_THICKNESS, padding=MIN_PADDING):
    box_list = top_line(width, border_thickness)
    box_list.append(empty_line(width, border_thickness))
    box_list.extend(text_line(text, width, border_thickness, padding))
    box_list.append(empty_line(width, border_thickness))
    box_list.extend(bottom_line(width, border_thickness))

    for line in box_list:
        print(line)

# # Examples
# print_in_box('')
# print_in_box('Ah, the past can hurt.')
# print_in_box("Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.")
# print_in_box('"You can fool all the people some of the time, and some of the people all of the time, but you can\'t fool all the people all the time." \n- Abraham Lincoln')