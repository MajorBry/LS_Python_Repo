import random
import os

DISPLAY_MARKS = (
    '\u2502', #0 vertical line '│'
    '\u2500', #1 horizontal line '─'
    '\u253c', #2 vertical/horizontal lines cross '┼'
    ' ',      #3 unused space
    'X',      #4 player symbol
    'O',      #5 computer symbol
    )
SQUARE_HORIZONTAL_LINES = 3
SQUARE_VERTICAL_LINES = 1
DISPLAY_VERTICAL_LINES = SQUARE_VERTICAL_LINES*3 + 2
WIN_GOAL =  5
WIN_MOVES = frozenset({frozenset({'A1', 'B1', 'C1'}),
                      frozenset({'A2', 'B2', 'C2'}),
                      frozenset({'A3', 'B3', 'C3'}),
                      frozenset({'A1', 'A2', 'A3'}),
                      frozenset({'B1', 'B2', 'B3'}),
                      frozenset({'C1', 'C2', 'C3'}),
                      frozenset({'A1', 'B2', 'C3'}),
                      frozenset({'C1', 'B2', 'A3'}),})

LINE_ROW = ' '*2 + DISPLAY_MARKS[1]*(SQUARE_HORIZONTAL_LINES) + DISPLAY_MARKS[2] + DISPLAY_MARKS[1]*SQUARE_HORIZONTAL_LINES + DISPLAY_MARKS[2] + DISPLAY_MARKS[1]*SQUARE_HORIZONTAL_LINES

EMPTY_ROW = DISPLAY_MARKS[3]*(SQUARE_HORIZONTAL_LINES + 2) + DISPLAY_MARKS[0] + DISPLAY_MARKS[3]*SQUARE_HORIZONTAL_LINES + DISPLAY_MARKS[0] + DISPLAY_MARKS[3]*SQUARE_HORIZONTAL_LINES

FIRST_MOVE_TUPLE = ('player', 'computer', 'choose')

def prompt(message):
    print(f'==> {message}')

def initialize_board():
    return {f'{row}{column}':DISPLAY_MARKS[3] for column in range(1,4)
                  for row in ['A', 'B', 'C']}
# ↑ Use ABC for rows and 123 for columns

def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_display(spaces, score):
    clear_display()
    print(f"  Player Score ({DISPLAY_MARKS[4]}): {score[DISPLAY_MARKS[4]]}\nComputer Score ({DISPLAY_MARKS[5]}): {score[DISPLAY_MARKS[5]]}\n")
    print('   1   2   3')
    print(f'A  {spaces['A1']} {DISPLAY_MARKS[0]} {spaces['A2']} {DISPLAY_MARKS[0]} {spaces['A3']} ')
    print(LINE_ROW)
    print(f'B  {spaces['B1']} {DISPLAY_MARKS[0]} {spaces['B2']} {DISPLAY_MARKS[0]} {spaces['B3']} ')
    print(LINE_ROW)
    print(f'C  {spaces['C1']} {DISPLAY_MARKS[0]} {spaces['C2']} {DISPLAY_MARKS[0]} {spaces['C3']} ')
    print('')

def get_user_move(options):
    while True:
        user_move = input("What's your move (e.g. 'A1')? ").upper()
        if user_move in options and options[user_move] == DISPLAY_MARKS[3]:
            return user_move
        else:
            prompt('Invalid move.')

"""
Problem:  create a function that determines if there is an imminent threat.
    Input:  dictionary, pointing to board
    Output:  string, of the key where the computer should go (empty if no imminent threat exists)
    Rules
        Explicit
            - An imminent threat occurs when the human player has 2 squares in a row with the 3rd square unoccupied
            - Computer reverts to random selection if no imminent threat exists
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases


Data Structures:  

Algorithm
    - if a two-member subset of a WIN_MOVES subset exists AND if the third member is empty, tell the computer to go there

    - make a player move set, having 'X' (DISPLAY_MARK[4])
    - loop through the WIN_MOVES set and check to see if the player move set has an intersection of length 2 with it

Implementation by Code
    - intersection (&) finds where two sets have common elements and returns those.  If the length of the resultant set is 2, AND if the last member is not occupied, the computer should be directed to move there
"""


def smart_comp_move(board):
    comp_moves = {move for move, val in board.items() if val == DISPLAY_MARKS[5]}
    for subset in WIN_MOVES:
        if len(comp_moves & subset) > 1 and board[next(iter((subset - comp_moves)))] == DISPLAY_MARKS[3]:
            return next(iter((subset - comp_moves)))

    player_moves = {move for move, val in board.items() if val == DISPLAY_MARKS[4]}
    for subset in WIN_MOVES:
        if len(player_moves & subset) > 1 and board[next(iter((subset - player_moves)))] == DISPLAY_MARKS[3]:
            return next(iter((subset - player_moves)))
    return None

def get_comp_move(options):
    comp_move = smart_comp_move(options)
    
    if not comp_move and options['B2'] == DISPLAY_MARKS[3]:
        comp_move = 'B2'

    if not comp_move:
        available_choices = [option for option, val in options.items() if val == DISPLAY_MARKS[3]]

        comp_move = random.choice(available_choices)

    prompt(f"Computer's move is: {comp_move}")
    return comp_move

def is_tie(board):
    return DISPLAY_MARKS[3] not in board.values()

def winner_mark(board):
    player_moves = {move for move, val in board.items() if val == DISPLAY_MARKS[4]}
    for subset in WIN_MOVES:
        if player_moves >= subset:
            return DISPLAY_MARKS[4]
    
    comp_moves = {move for move, val in board.items() if val == DISPLAY_MARKS[5]}
    for subset in WIN_MOVES:
        if comp_moves >= subset:
            return DISPLAY_MARKS[5]
    
    if is_tie(board):
        return DISPLAY_MARKS[3]

    return None

def display_winner(mark=None):
    if mark == DISPLAY_MARKS[4]:
        prompt('Player wins!')
    elif mark == DISPLAY_MARKS[5]:
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

def display_match_winner(mark=None):
    if mark == DISPLAY_MARKS[4]:
        prompt('Player wins the match!')
    elif mark == DISPLAY_MARKS[5]:
        prompt('Computer wins the match!')
    
def play_again(message="Do you want to play again? (y/n): "):
    answer = input(message)
    if answer.casefold() in {'n', 'no'}:
        return False
    else:
        return True

def user_move(board):
    board[get_user_move(board)] = DISPLAY_MARKS[4]

def comp_move(board):
    board[get_comp_move(board)] = DISPLAY_MARKS[5]

def initialize_score():
    return {DISPLAY_MARKS[4]:0,
            DISPLAY_MARKS[5]:0,
            DISPLAY_MARKS[3]:0,}

def moves(board, score, first):
    
    if first == FIRST_MOVE_TUPLE[0]:
        user_move(board)
    else:
        comp_move(board)
    update_display(board, score)

    if winner_mark(board):
        winner = winner_mark(board)
        score[winner] += 1
        update_display(board, score)
        display_winner(winner)
        return 'break'
    elif first == FIRST_MOVE_TUPLE[0]:
        comp_move(board)
        update_display(board, score)
    else:
        user_move(board)
        update_display(board, score)

    if winner_mark(board):
        winner = winner_mark(board)
        score[winner] += 1
        update_display(board, score)
        display_winner(winner)
        return 'break'

def get_first_move():
    while True:
        answer = input('Who should go first during this match?\n1 - player\n2 - computer\n3 - random\n')

        if answer not in {'1', '2', '3'}:
            print('Invalid entry.')
        else:
            match answer:
                case '1':
                    return FIRST_MOVE_TUPLE[0]
                case '2':
                    return FIRST_MOVE_TUPLE[1]
                case '3':
                    return random.choice([FIRST_MOVE_TUPLE[0], FIRST_MOVE_TUPLE[1]])

# Initialize display
score = initialize_score()

first_move_pick = FIRST_MOVE_TUPLE[2]
if first_move_pick == FIRST_MOVE_TUPLE[2]:
        first_move = get_first_move()

while True:
    board = initialize_board()

    while True:
        update_display(board, score)

        if moves(board, score, first_move):
            break
    
    if score[winner_mark(board)] >= WIN_GOAL:
        update_display(board, score)
        display_match_winner(winner_mark(board))
        if not play_again("Do you want to start a new match? ('n' or 'no' to exit): "):
            prompt('Goodbye!')
            break
        score = initialize_score()
        if first_move_pick == FIRST_MOVE_TUPLE[2]:
            first_move = get_first_move()
    else:
        if not play_again("Move on to the next round? ('n' or 'no' to exit): "):
            prompt('Goodbye!')
            break
    update_display(board, score)