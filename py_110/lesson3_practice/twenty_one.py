"""
Problem:  Implement code for the game 21.
    Input:  strings, user input
    Output:  print to screen
    Rules
        Explicit
            - deck has standard playing cards
            - each suite (♥, ♦, ♣, ♠) has 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
            - numbered cards have their face value
            - Ace is 1 or 11
            - Jack, Queen, and King are 10
            - Dealer (computer) must hit at least 17
            - a total of over 21 is a bust (lose)
            - Player only sees one of the dealer's cards and must choose how much to hit before the dealer takes their turns
            - if player busts, they lose
            - if dealer busts, they lose
            - if neither busts, but finish their turns, whoever has the highest value total wins
        Implicit
            - Dealer will hit if total is less than player total
    Questions
        - ()

Examples/ Test Cases


Data Structures:  dictionary of cards, card_names:values.

Algorithm
    - Step-by-step
        1. shuffle deck (randomized)
        2a. dealer draws 2 cards (1 face up)
        2b. player draws 2 cards (2 face up)
        3. display cards
        4. player chooses whether to hit or stay, if player stays go to 9
        *5. player hits: draws a new card from deck
        *6. display new card
        *7. sum values of player cards (check aces)
        *8. check if player loses, if so go to 14, else return to 4
        9. dealer chooses whether to stay, if dealer stays go to 14
        *10. dealer hits: draws a new card from deck
        *11. display new card
        *12. sum values of dealer cards (check aces)
        *13. check if dealer loses, if so go to 14, else return to 9
        14. display winner
        15. play again?
        16. goodbye
    
    Step-by-step (v2):
        1. display a welcome message
        1a. offer the player to view the rules at any point (keep a reminder in header or footer)
            - if player decides whether to view rules:
                - if yes, view rules:
                    i.  clear screen
                    ii.  show rules
                    iii.  player continues by pushing enter
        1b. player must press enter to continue on to the game.
        2. display initial cards
            i.  initialize deck
            ii.  add 2 cards randomly from deck to dealer
            iii.  add 2 cards randomly from deck to player
            iv.  only show 1 of the cards of the dealer and the back of the card
            v.  show both player cards
        2a. display dealer cards with dealer caption (could do an ascii-art dealer)
        2b. display player cards with player caption
        3. player turn: ask for player to hit or stay
            - if hit:
                i.  add 1 card randomly from deck to player
                ii.  declare the card drawn
                iii.  display updated cards
                iv.  determine if player busted
                    - if player busted:
                        a.  announce the dealer as the winner
                        b.  ask if the player would like to play again
                    - if player did not bust: return to 3 (hit or stay?)
        4. dealer turn: determine if the dealer has won.
            - if dealer won:
                i.  announce the dealer as the winner
                ii.  ask if the player wants to play again
            - if dealer has not won AND dealer score is less than 17: dealer hits
                + if dealer busted:
                    a.  announce the player as the winner
                    b.  ask if the player would like to play again
                + if dealer has not busted: repeat 4
            - else (dealer score is at least 17) determine if there is a tie:
                + if player and dealer tie:
                    i.  announce the tie
                    ii.  ask if the player wants to play again
                + if there is no tie (player had a higher score than dealer):
                    a.  announce the player as the winner
                    b.  ask if the player would like to play again
        5. Good bye: player does not want to play again
        5a. goodbye message prints

Implementation by Code
    - Use random.choice and available cards from deck
    - When a card is drawn, replace value with None in deck
"""
import random
import os

CARD_VALUES = {'2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  '10': 10,
                  'J': 10, # ← Jack
                  'Q': 10, # ← Queen
                  'K': 10, # ← King
                  'A': 11, # ← Ace
                  }

DISPLAY_MARKS = (
    '\u2665', #0 '♥' heart: h
    '\u2666', #1 '♦' diamond: d
    '\u2663', #2 '♣' club: c
    '\u2660', #3 '♠' spade: s
    '\u2502', #4 vertical line '│'
    '\u2500', #5 horizontal line '─'
    '\u256d', #6 '╭'
    '\u256e', #7 '╮'
    '\u2570', #8 '╰'
    '\u256f', #9 '╯'
    ' ', #10 ' '
    '@', #11 card symbol placeholder
    '\u2573', #12 back of card
)

FLOW_COMMANDS = ('continue', 'restart', 'end')

WINS_FOR_MATCH = 3

PEAK_SCORE = 21
ACE_MODIFIER = 10
DEALER_MIN_SCORE = 17 # ← Dealer will continue to hit until they reach or exceed this number

CARD_WIDTH = 9 # inner width
SPACE_BETWEEN_CARDS = '  '

CARD_TOP_LINES = SPACE_BETWEEN_CARDS + DISPLAY_MARKS[6] + DISPLAY_MARKS[5]*CARD_WIDTH + DISPLAY_MARKS[7]

CARD_BOTTOM_LINES = SPACE_BETWEEN_CARDS + DISPLAY_MARKS[8] + DISPLAY_MARKS[5]*CARD_WIDTH + DISPLAY_MARKS[9]

BLANK_LINES = SPACE_BETWEEN_CARDS + DISPLAY_MARKS[4] + DISPLAY_MARKS[10]*CARD_WIDTH + DISPLAY_MARKS[4]

BACK_CARD_LINES = SPACE_BETWEEN_CARDS + DISPLAY_MARKS[4] + DISPLAY_MARKS[12]*CARD_WIDTH + DISPLAY_MARKS[4]

TOP_BLANK_LINE = SPACE_BETWEEN_CARDS + DISPLAY_MARKS[4] + DISPLAY_MARKS[10]*(CARD_WIDTH - 2) + DISPLAY_MARKS[11] + DISPLAY_MARKS[10] + DISPLAY_MARKS[4]

BOTTOM_BLANK_LINE = SPACE_BETWEEN_CARDS + DISPLAY_MARKS[4] + DISPLAY_MARKS[10] + DISPLAY_MARKS[11] + DISPLAY_MARKS[10]*(CARD_WIDTH - 2) + DISPLAY_MARKS[4]

def initialize_deck():
    return {(face + symbol):val
     for face, val in CARD_VALUES.items()
     for symbol in DISPLAY_MARKS[:4]}

def draw_cards(deck, number):
    available_cards = {card:val for card, val in deck.items() if val}
    drawn_cards = {}
    for _ in range(number):
        card = random.choice(list(available_cards.keys()))
        drawn_cards[card] = available_cards[card]
        deck[card] = None
        available_cards.pop(card)
    return drawn_cards

def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_display(game_state):
    dealer_hand, player_hand, turn = (game_state['dealer hand'], game_state['player hand'], game_state['flow state']['turn'])
    clear_display()
    num_dealer_hand = len(dealer_hand)
    num_player_hand = len(player_hand)

    print('')
    print(f'- Dealer ({game_state['match points']['dealer']} wins) -'.center(num_dealer_hand*(CARD_WIDTH + 5)))
    print((CARD_TOP_LINES)*num_dealer_hand)
    skip = True
    for card_name in dealer_hand:
        if turn == 'player' and skip:
            print(BLANK_LINES,end='')
            skip = False
        else:
            print(TOP_BLANK_LINE.replace(DISPLAY_MARKS[11], card_name[-1]),end='')
    print('')
    print(BLANK_LINES*num_dealer_hand)
    skip = True
    for card_name in dealer_hand:
        if turn == 'player' and skip:
            print(BLANK_LINES,end='')
            skip = False
        else:
            print(SPACE_BETWEEN_CARDS + DISPLAY_MARKS[4] + card_name[:-1].center(CARD_WIDTH) + DISPLAY_MARKS[4],end='')
    print('')
    print(BLANK_LINES*num_dealer_hand)
    skip = True
    for card_name in dealer_hand:
        if turn == 'player' and skip:
            print(BLANK_LINES,end='')
            skip = False
        else:
            print(BOTTOM_BLANK_LINE.replace(DISPLAY_MARKS[11], card_name[-1]),end='')
    print('')
    print((CARD_BOTTOM_LINES)*num_dealer_hand)
    print('')

    print(f'- Player ({game_state['match points']['player']} wins) -'.center(num_dealer_hand*(CARD_WIDTH + 5)))
    print((CARD_TOP_LINES)*num_player_hand)
    for card_name in player_hand:
        print(TOP_BLANK_LINE.replace(DISPLAY_MARKS[11], card_name[-1]),end='')
    print('')
    print(BLANK_LINES*num_player_hand)
    for card_name in player_hand:
        print(SPACE_BETWEEN_CARDS + DISPLAY_MARKS[4] + card_name[:-1].center(CARD_WIDTH) + DISPLAY_MARKS[4],end='')
    print('')
    print(BLANK_LINES*num_player_hand)
    for card_name in player_hand:
        print(BOTTOM_BLANK_LINE.replace(DISPLAY_MARKS[11], card_name[-1]),end='')
    print('')
    print((CARD_BOTTOM_LINES)*num_player_hand)
    print('')

def card_name(card):
    symbol = list(card.keys())[0][-1]
    match symbol:
        case '\u2665':
            symbol = 'hearts'
        case '\u2666':
            symbol = 'diamonds'
        case '\u2663':
            symbol = 'clubs'
        case '\u2660':
            symbol = 'spades'
        case _:
            print('Error.')
            return None

    name = list(card.keys())[0][:-1]
    match name:
        case 'J':
            name = 'Jack'
        case 'Q':
            name = 'Queen'
        case 'K':
            name = 'King'
        case 'A':
            name = 'Ace'
    return f"{name} of {symbol}"

def get_player_move(game_state):
    deck, player_hand, flow_state = (game_state['deck'], game_state['player hand'], game_state['flow state'])
    print("Player's Turn".center(30,) + "\n")
    while True:
        answer = player_input(game_state, "Will you hit or stay? (hit/stay): ").casefold()
        if answer in {'h', 'hit'}:
            new_card = draw_cards(deck, 1)
            player_hand |= new_card
            update_display(game_state)
            print(f"You drew the {card_name(new_card)}.")

            if is_busted(player_hand):
                game_state['match points']['dealer'] += 1
                update_display(game_state)
                print(f"You drew the {card_name(new_card)}.")
                print("You bust!")
                if game_state['match points']['dealer'] > 2:
                    print('Dealer wins the match! better luck next time!')
                else:
                    print('Dealer wins!')
                play_again(game_state)
                return
        elif answer in {'s', 'stay'}:
            flow_state['turn'] = 'dealer'
            return
        else:
            print("Input invalid. Type 'h', 'hit', 's', or 'stay' and hit 'Enter'")

def calculate_score(cards):
    score = sum(cards.values())
    for card in cards.keys():
        if score > PEAK_SCORE:
            if card[0] == 'A': # ← A (Ace)
                score -= ACE_MODIFIER
    return score

def get_dealer_move(game_state):
    deck, dealer_hand, player_hand = (game_state['deck'], game_state['dealer hand'], game_state['player hand'])

    player_score = calculate_score(player_hand)

    print("Dealer's Turn".center(30,) + "\n")

    while True:
        dealer_score = calculate_score(dealer_hand)
        # ↓ Check for winner dealer's score is > or == player's
        if dealer_score >= DEALER_MIN_SCORE:
            if dealer_score > player_score:
                game_state['match points']['dealer'] += 1
                update_display(game_state)
                if game_state['match points']['dealer'] > 2:
                    print('Dealer wins the match! better luck next time!')
                else:
                    print('Dealer wins!')
                play_again(game_state)
            elif dealer_score == player_score:
                print('Tie game!')
                play_again(game_state)
            else:
                game_state['match points']['player'] += 1
                update_display(game_state)
                if game_state['match points']['player'] > 2:
                    print('Congratulations! You win the match!')
                else:
                    print('You win!')
                play_again(game_state)
            return

        wait(game_state)

        new_card = draw_cards(deck, 1)
        dealer_hand |= new_card
        update_display(game_state)
        print("Dealer's Turn".center(30,) + "\n")
        print(f"Dealer drew the {card_name(new_card)}.")

        if is_busted(dealer_hand):
            game_state['match points']['player'] += 1
            update_display(game_state)
            print("Dealer busts!")
            if game_state['match points']['player'] > 2:
                print('Congratulations! You win the match!')
            else:
                print('You win!')
            play_again(game_state)
            return

def is_busted(cards):
    score = calculate_score(cards)
    return score > PEAK_SCORE

def play_again(game_state):
    flow_state = game_state['flow state']
    answer = player_input(game_state, "Do you want to play again? ('n'/'no' to exit) ").casefold()

    if answer not in {'n', 'no'}:
        flow_state['command'] = FLOW_COMMANDS[1]
        return

    flow_state['command'] = FLOW_COMMANDS[2]
    return

def prompt(message):
    print('==> ' + message)

def player_input(game_state, message=''):
    answer = input(message)

    if answer.casefold() in {'rules', 'r'}:
        show_rules(game_state)

    if answer.casefold() in {'quit', 'exit'}:
        quit()

    return answer

def wait(game_state):
    return player_input(game_state, "Press 'Enter' to continue.\n\n")

def show_rules(game_state):
    clear_display()

    RULEBOOK = {
                'deck': "Start with a standard 52-card deck consisting of the 4 suits (Hearts, Diamonds, Clubs, and Spades), and 13 values (2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace).",
                'goal': "The goal of Twenty-One is to try to get as close to 21 as possible without going over. If you go over 21, it's a bust, and you lose.",
                'setup': "The game consists of a dealer (computer) and a player. Both participants are initially dealt a hand of two cards. The player can see their two cards, but can only see one of the dealer's cards.",
                'card values': "All of the card values are pretty straightforward, except for the Ace. The cards with numbers 2 through 10 are worth their face value. The Jack, Queen, and King are each worth 10. The Ace can be worth 1 or 11 depending on circumstances. Its value is determined each time a new card is drawn from the deck. For example, if the hand contains a 2, an Ace, and a 5, then the total value of the hand is 18. In this case, the Ace is worth 11 because the sum of the hand (2 + 11 + 5) doesn't exceed 21. Now, say another card is drawn, and it happens to be an Ace. If the sum of the hand (2 + 11 + 5 + 11) exceeds 21, then one of the Aces must be worth 1, resulting in the hand's total value being 19.",
                }
    print('    - Rules of 21 -    \n')
    for heading, section in RULEBOOK.items():
        print(heading.capitalize() + ':')
        print(section)
        print('')

    wait(game_state)
    update_display(game_state)

# ↓ Contains deck, player hand, dealer hand, etc.

def initialize_game_state(match_points=None):
    if match_points == None:
        match_points = {
            'player': 0,
            'dealer': 0,
        }

    game_state = {
              'deck': initialize_deck(),
              'dealer hand': {},
              'player hand': {},
              'flow state': {
                  'turn': 'player',
                  'command': FLOW_COMMANDS[0],
              },
              'match points': match_points
              }
    return game_state

clear_display()
prompt("Welcome to the game of 21!\nFeel free to review the rules at any time during the game by typing 'rules' and pressing Enter.")

game_state = initialize_game_state()
answer = wait(game_state)

while True:
    match_points = None

    # ↓ Main game loop
    while True:
        game_state = initialize_game_state(match_points)
        match_points = game_state['match points']
        deck = game_state['deck']
        dealer_hand = game_state['dealer hand']
        player_hand = game_state['player hand']
        flow = game_state['flow state']

        dealer_hand |= draw_cards(deck, 2)

        player_hand |= draw_cards(deck, 2)

        update_display(game_state)
        get_player_move(game_state) # ← display state command will be 'restart', 'end', or 'continue' after this line

        if flow['command'] == FLOW_COMMANDS[0]:
            update_display(game_state)
            get_dealer_move(game_state)

        if flow['command'] == FLOW_COMMANDS[2]:
            break

        if WINS_FOR_MATCH in match_points.values():
            break

    if flow['command'] == FLOW_COMMANDS[2]:
        break
