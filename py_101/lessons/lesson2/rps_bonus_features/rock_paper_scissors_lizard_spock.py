import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WIN_CHOICES = {
    'rock':['scissors', 'lizard'],
    'paper':['rock', 'spock'],
    'scissors':['paper', 'lizard'],
    'lizard':['spock', 'paper'],
    'spock':['rock', 'scissors'],
    }
NUMBER_TO_WIN = 3

def prompt(message):
    print(f'==> {message}')

def determine_winner(player, computer):
    if computer in WIN_CHOICES[player]:
        return 'player'
    elif player in WIN_CHOICES[computer]:
        return 'computer'
    else:
        return 'tie'

def choose():
    def short_answer(text):
        for option in VALID_CHOICES:
            if option.startswith(text.casefold()) and text:
                return option
        return None

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = short_answer(input())

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = short_answer(input())
    return choice

p_win = 0
c_win = 0

while True:
    prompt(f'Round {p_win + c_win + 1}')
    player_choice = choose()
    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {player_choice}, computer chose {computer_choice}")
    winner = determine_winner(player_choice, computer_choice)

    if winner == 'player':
        p_win += 1
        prompt(f'You win the round! Player: {p_win} / Computer: {c_win}')
    elif winner == 'computer':
        c_win += 1
        prompt(f'Computer wins the round! Player: {p_win} / Computer: {c_win}')
    else:
        prompt(f'Tie round! Player: {p_win} / Computer: {c_win}')

    if p_win >= NUMBER_TO_WIN:
        prompt('You are the grand winner!')
    elif c_win >= NUMBER_TO_WIN:
        prompt('Computer is the grand winner!')
    else:
        continue

    while True:
        prompt('Do you want to play again (y/n)?')
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            p_win = 0
            c_win = 0
            break
        else:
            prompt("That's not a valid choice")
    if answer[0] == 'n':
        break
