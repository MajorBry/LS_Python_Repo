import json
import ex_03_bannerizer as banner

STORY_SELECTION = 'example 1'

# Open the JSON file for reading
with open('/home/bry/my_linux_files/LS_Python_Repo/py_101/exercises/easy3/ex_06_stories.json', 'r') as file:
    STORY_FILE = json.load(file)[STORY_SELECTION]
STORY = STORY_FILE[0]
INPUTS = tuple(STORY_FILE[1])

def input_prompt(text):
    return input('>> ' + text)

def prompt(text):
    print('>> ' + text)

def invalid_string(string):
    if string == '':
        return True
    try:
        int(string)
    except ValueError:
        try:
            float(string)
        except ValueError:
            return False
    return True

def get_input(prompt_string, word):
    user_input = input_prompt(f'{prompt_string}{word}: ')
    while invalid_string(user_input):
        prompt('Invalid input')
        user_input = input_prompt(f'{prompt_string}{'n' if word[0] == 'a' else ''} {word}: ')
    return user_input

story_list = STORY.split('##')

inputs_dict = {}
for word_type in INPUTS:
    inputs_dict[word_type] = get_input(f'Enter a{'n' if word_type == 'a' else ''} ', word_type)

for element in INPUTS:
    while True:
        try:
            story_list.index(element)
        except ValueError:
            break
        story_list[story_list.index(element)] = inputs_dict[element]

banner.print_in_box(''.join(story_list))
