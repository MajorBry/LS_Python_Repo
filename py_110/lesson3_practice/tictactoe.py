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

LINE_ROW = ' '*2 + DISPLAY_MARKS[1]*(SQUARE_HORIZONTAL_LINES) + DISPLAY_MARKS[2] + DISPLAY_MARKS[1]*SQUARE_HORIZONTAL_LINES + DISPLAY_MARKS[2] + DISPLAY_MARKS[1]*SQUARE_HORIZONTAL_LINES

EMPTY_ROW = DISPLAY_MARKS[3]*(SQUARE_HORIZONTAL_LINES + 2) + DISPLAY_MARKS[0] + DISPLAY_MARKS[3]*SQUARE_HORIZONTAL_LINES + DISPLAY_MARKS[0] + DISPLAY_MARKS[3]*SQUARE_HORIZONTAL_LINES

def prompt(message):
    print(f'==> {message}')

def initialize_board():
    return {f'{row}{column}':DISPLAY_MARKS[3] for column in range(1,4)
                  for row in ['A', 'B', 'C']}
# ↑ Use ABC for rows and 123 for columns

def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_display(spaces):
    clear_display()
    print(f"Tic-Tac-Toe (Player: {DISPLAY_MARKS[4]}) (Computer: {DISPLAY_MARKS[5]})\n")
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

def get_comp_move(options):
    available_choices = [option for option, val in options.items() if val == DISPLAY_MARKS[3]]
    comp_move = random.choice(available_choices)
    prompt(f"Computer's move is: {comp_move}")
    return comp_move

def is_tie(board):
    return DISPLAY_MARKS[3] not in board.values()

def winner_mark(moves):
    WIN_MOVES = {frozenset({'A1', 'B1', 'C1'}),
                      frozenset({'A2', 'B2', 'C2'}),
                      frozenset({'A3', 'B3', 'C3'}),
                      frozenset({'A1', 'A2', 'A3'}),
                      frozenset({'B1', 'B2', 'B3'}),
                      frozenset({'C1', 'C2', 'C3'}),
                      frozenset({'A1', 'B2', 'C3'}),
                      frozenset({'C1', 'B2', 'A3'}),}
        
    player_moves = {move for move, val in moves.items() if val == DISPLAY_MARKS[4]}
    for subset in WIN_MOVES:
        if player_moves >= subset:
            return DISPLAY_MARKS[4]
    
    comp_moves = {move for move, val in moves.items() if val == DISPLAY_MARKS[5]}
    for subset in WIN_MOVES:
        if comp_moves >= subset:
            return DISPLAY_MARKS[5]
    
    if is_tie(moves):
        return DISPLAY_MARKS[3]

    return None

def display_winner(mark=None):
    if mark == DISPLAY_MARKS[4]:
        prompt('Player wins!')
    elif mark == DISPLAY_MARKS[5]:
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

def play_again():
    answer = input("Do you want to play again? (y/n): ")
    if answer.casefold() in {'y', 'yes'}:
        return True
    else:
        return False

def user_move(board):
    board[get_user_move(board)] = DISPLAY_MARKS[4]

def comp_move(board):
    board[get_comp_move(board)] = DISPLAY_MARKS[5]

# Initialize display
board = initialize_board()

while True:
    update_display(board)

    user_move(board)
    update_display(board)

    if winner_mark(board):
        display_winner(winner_mark(board))
        if play_again():
            board = initialize_board()
        else:
            prompt('Goodbye!')
            break
    else:
        comp_move(board)
        update_display(board)

    if winner_mark(board):
        display_winner(winner_mark(board))
        if play_again():
            board = initialize_board()
        else:
            prompt('Goodbye!')
            break
