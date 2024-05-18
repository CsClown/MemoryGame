import os
import time
import random
import re
import getpass

# our card symbols
# heart = '\u2665'
# star = '\u2605'
# music = '\u266b'
# sun = '\u2600'
# cloud = '\u2601'
# umbrella = '\u2602'
# soccer_ball = '\u26bd'
# basketball = '\U0001F3C0'

joker = '\U0001F0CF'
watermelon = '\U0001f349'
rose = '\U0001f339'
cake = '\U0001f370'
lollipop = '\U0001f36d'
soft_ice_cream = '\U0001f366'
four_leaf_clover = '\U0001f340'
glowing_star = '\U0001f31f'
eggplant = '\U0001f346'

ascii_symbol_list = [
    watermelon,
    rose,
    cake,
    lollipop,
    soft_ice_cream,
    four_leaf_clover,
    glowing_star,
    eggplant
]

col_labels = ['A','B','C','D']
row_labels = ['0', '1', '2', '3']



class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.pairs = []
        self.pick1 = []
        self.pick2 = []
        self.active = True

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score
    
    def get_pairs(self):
        return self.pairs

    def add_pair(self, pair):
        self.pairs.append(pair)

player1 = player('user')
player2 = player('Computer')
player2.active = False


def clear_terminal():
    """
    Clears terminal for anti-cheat and overall clarity
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_instructions():
    """
    Display the game instructions
    """
    print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##     ## ######## ##     ##  #######  ########  ##    ## 
###   ### ##       ###   ### ##     ## ##     ##  ##  ##  
#### #### ##       #### #### ##     ## ##     ##   ####   
## ### ## ######   ## ### ## ##     ## ########     ##    
##     ## ##       ##     ## ##     ## ##   ##      ##    
##     ## ##       ##     ## ##     ## ##    ##     ##    
##     ## ######## ##     ##  #######  ##     ##    ##

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)

    enter = getpass.getpass('\nPress "ENTER" to continue..')
    if enter == '':
        clear_terminal()
        
    

    print("""
    +++ Memory Game Instructions 1/2 +++

                **Objective:**
    The goal of the memory (concentration) game is to find all matching pairs
    of cards on a 4x4 board in the fewest moves possible.

                **Setup:**
    1. The game board consists of 16 cards arranged in a 4x4 grid.
    2. Each card has a matching pair hidden somewhere on the board.

                **How to Play:**
    1. On your turn, flip over any two cards by selecting their positions
        on the board (e.g., A1 and B2).
    2. If the two cards match, they get added to your stash and removed
        from the board. You get another turn after finding a pair.
    3. If the cards do not match, they are turned back face down after 
        a brief pause, and then your opponent takes his turn.
    4. Continue flipping two cards at a time until all pairs are found 
        and matched.""")

    enter = getpass.getpass('\nPress "ENTER" to continue..')
    if enter == '':
        clear_terminal()

    print("""
    +++ Memory Game Instructions 2/2 +++

                **Winning the Game:**
    - The game is won when all pairs of cards have been successfully
        matched, removed from the board and added to the stashes of
        the players
   
                **Tips:**
    - Pay close attention to the positions and values of the cards you 
        flip over.
    - Use your memory to remember the locations of cards to find pairs
        more efficiently.""")

    enter = getpass.getpass('\nPress "ENTER" to continue..')
    if enter == '':
        clear_terminal()
    

def initialize_board(size = 4, symbols = None):
    """
    Initializes the board with random order of symbols
    with optional custom size and symbols list
    """
    if symbols == None: 
        symbols = ascii_symbol_list.copy()
    duplicates = []
    board = []
    row = []
    for i in range(size):
        row = []
        for j in range(size):
            symbol = random.choice(symbols)
            row.append(symbol)
            if symbol in duplicates:
                symbols.remove(symbol)
            duplicates.append(symbol)
        board.append(row)
    return board

board = initialize_board()

def draw_board(board, player, pick1 = None, pick2 = None):
    """
    Draw the board depending on game state
    with either one, two or no card revealed
    """
    clear_terminal()
    if (player.name != 'Computer'):
        print(f"+++ {player.name} +++")
        print(f"### Current score: {player.score} ###")
        if player.pairs != []:
            print('Your stash:', end = " ") 
            for i in range(len(player.pairs)):
                print(player.pairs[i]*2, end = " ")
            print('\n')
    else: 
        print("+++ Computer +++")
        print(f"### Current score: {player.score} ###")
        if player.pairs != []:
            print('Computers stash:', end = " ")
            for i in range(len(player.pairs)):
                print(player.pairs[i]*2, end = " ")
            print('\n')
    print('\n' + '-' * 25 )
    print(' '* 5 + 'A' + ' ' * 4 + 'B' + ' ' * 4 + 'C' + ' ' * 4 + 'D')
    for x in range(len(board)):
        print(f'\n\n{x}    ', end = '')
        
        for y in range(len(board[0])):
            if board[x][y] == '0':
                print(' ', end = '    ')
            elif pick1 and pick1 == [y,x]:
                print(board[x][y], end = '    ')
            elif pick2 and pick2 == [y,x]:
                print(board[x][y], end = '    ')
            else: print(joker, end = '    ')
    print('\n' + '-' * 25 )
    print('\n')
    
    

def validate_input(pick):
    """
    validate user input (list)
    """
    try: 
        if len(pick) != 2:
            raise ValueError(
                f'Exactly 2 values required, you provided {len(pick)}'
            )
        elif pick[0].upper() not in col_labels:
            raise ValueError(
                f'Please pick a letter A - D, you provided "{pick[0].upper()}"'
            )
        elif pick[1] not in row_labels:
            raise ValueError(
                f'Please pick a number 0-3, you provided "{pick[1]}"'
            )
        elif board[int(pick[1])][ord(pick[0].upper()) - 65] == '0':
            raise ValueError(
                f'Field {pick} is empty '
            )
    except ValueError as e:
        print('\n')
        print('--->', end = ' ')
        print(f'Invalid data: {e}, please try again')
        print('\n')
        return False
    else: return True



def player_turn(player):
    """
    Facilitates a whole turn of the active player
    """

    cards = pick_cards(player)
    if check_pair(cards):
        symbol = board[cards[0][1]][cards[0][0]]
        player.add_score()
        player.add_pair(symbol)
        remove_pair(symbol)
        if player.name == 'Computer':
            print(f'+++ The Computer got a pair: {symbol}{symbol} !! +++')
        else: print(f'+++ You got a pair: {symbol}{symbol} !! +++')
        
        if player1.score + player2.score < 8:
            if player.name == 'Computer':
                print('Computer gets another turn!')
            else: print('You get another turn!')
            print('\n')
        else:
            print("That was the last two cards! let's check the scores")
            print('\n')
            print('.', end = '', flush = True)
            time.sleep(0.2)
            print('.', flush = True)
            time.sleep(0.2)

    else: 
        player.active = False
        if player.name == "Computer":
            print(f'+++ The Computer has no pair! Your turn again, {player1.name}.. +++', flush = True)
            print('\n')
            player1.active = True
        else: 
            player2.active = True
            print("+++ Sorry! No pair :( Computer's turn now +++", flush = True)
            print('\n')
        time.sleep(1)
        
        
        
    player.pick1 = []
    player.pick2 = []

    enter = getpass.getpass('Press "ENTER" to continue..')
    if enter == '':
        pass


def pick_cards(player):
    """
    User Input for choosing a card on the board
    calls validate_input for input validation ;)
    returns list
    """
    card1 = None
    card2 = None

    while True:
        if player.name == 'Computer':
            while card1 == None or board[card1[1]][card1[0]] == '0':
                x1 = random.choice(col_labels)
                y1 = random.randint(0, 3)
                player.pick1 = [x1,y1]
                card1 = [ord(player.pick1[0]) - 65, player.pick1[1]]
            while card2 == None or card2 == card1 or board[card2[1]][card2[0]] == '0':
                x2 = random.choice(col_labels)
                y2 = random.randint(0, 3)
                player.pick2 = [x2,y2]     
                card2 = [ord(player.pick2[0]) - 65, player.pick2[1]]

            print('The Computer is thinking..')
            print('.', end = '', flush = True)
            time.sleep(0.2)
            print('.', end = '', flush = True)
            time.sleep(0.2)
            print(f'The Computers first pick is: {player.pick1[0]}{player.pick1[1]}')
            time.sleep(2)
            
            draw_board(board, player, card1)
            print('The Computer is thinking..')
            print('.', end = '', flush = True)
            time.sleep(0.2)
            print('.', end = '', flush = True)
            time.sleep(0.2)
            print(f'The Computers second pick is: {player.pick2[0]}{player.pick2[1]}')
            time.sleep(1)
            
            draw_board(board, player, card1, card2)
            time.sleep(2)
            break
        if player.pick1 == []:
            print('+++ Please pick your FIRST card! Example: A1 +++\n') 
            pick_str = input('+++ YOUR PICK: ')
            pick_strip = [i.strip() for i in pick_str]
            pick_ls = [string for string in pick_strip]
            if validate_input(pick_strip):
                player.pick1 = [pick_strip[0].upper(),int(pick_strip[1])]
                print(f'You chose: {player.pick1[0]}{player.pick1[1]}')
                card1 = [ord(player.pick1[0]) - 65, player.pick1[1]]
                draw_board(board, player, card1)
        elif player.pick2 == []:
            print('+++ Please pick your SECOND card! Example: A1 +++\n') 
            pick_str = input('+++ YOUR PICK: ')
            pick_strip = [i.strip() for i in pick_str]
            pick_ls = [string for string in pick_strip]
            if validate_input(pick_strip):
                player.pick2 = [pick_strip[0].upper(),int(pick_strip[1])]
                if player.pick2 == player.pick1:
                    print('+++ You cannot choose the same card twice! +++')
                    player.pick2 = []
                    continue
                print(f'You chose: {player.pick2[0]}{player.pick2[1]}')
                card2 = [ord(player.pick2[0]) - 65, player.pick2[1]]
                draw_board(board, player, card1, card2)
                time.sleep(2)
                break
    return card1, card2

def check_pair(cards):
    if board[cards[0][1]][cards[0][0]] == board[cards[1][1]][cards[1][0]]:
        return True
    else:
        return False

def remove_pair(symbol):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == symbol:
                board[x][y] = '0'
    
def end_of_game():
    if player1.score + player2.score == 8:
        clear_terminal()
        print('\n+++ Game over +++\n')
        if player1.score > player2.score: 
            print(f"Congratulations, {player1.name}! \nYou won with {player1.score} points\n")
            print(f"Your pairs: ")
            for i in range(len(player1.pairs)):
                print(player1.pairs[i], end = " ")
                print(player1.pairs[i], end = " ")
            print('\n')
            print(f"The computers pairs: ")
            for i in range(len(player2.pairs)):
                print(player2.pairs[i], end = " ")
                print(player2.pairs[i], end = " ")

        elif player1.score == player2.score:
            print(f"Well it's a draw!")
            print(f"Your pairs: ")
            for i in range(len(player1.pairs)):
                print(player1.pairs[i], end = " ")
                print(player1.pairs[i], end = " ")
            print(f"\nThe computers pairs: ")
            for i in range(len(player2.pairs)):
                print(player2.pairs[i], end = " ")
                print(player2.pairs[i], end = " ")
        else:
            print(f'The Computer has beaten you with {player2.score} to {player1.score} points\n')
            print(f"The computers pairs: ")
            for i in range(len(player2.pairs)):
                print(player2.pairs[i], end = " ")
                print(player2.pairs[i], end = " ")
            print(f"\nYour pairs: ")
            for i in range(len(player1.pairs)):
                print(player1.pairs[i], end = " ")
                print(player1.pairs[i], end = " ")
            print('\n')
        print('\n')
        print('+'*17)
        while True:
            try:
                choice = input('Do you want to play again? y/n \n')
                if choice.upper() != 'N' and choice.upper() != 'Y':
                    raise ValueError(
                        f'Only "y" or "n" allowed.. you entered "{choice}"'
                    )
                elif choice.upper() == 'Y':
                    global board
                    board = initialize_board()
                    player1.score = 0
                    player1.pairs = []
                    player1.pick1 = []
                    player1.pick2 = []
                    player1.active = True
                    player2.score = 0
                    player2.pairs = []
                    player2.pick1 = []
                    player2.pick2 = []
                    player2.active = False
                    clear_terminal()
                    print("Let's start a fresh game :)", flush = True)
                    print("Initializing.", end = '', flush = True)
                    time.sleep(1)
                    print('.', end = '', flush = True)
                    time.sleep(1)
                    print('.', end = '', flush = True)
                    return False

                elif choice.upper() == 'N':
                    return True
            except ValueError as e:
                print(f'Invalid Data: {e}! Please try again')
                
def name_input():
    """
    Validates user input and returns username
    """
    while True:
        username = input('Please tell me your name: ')
        if not username:
            print('Name cannot be empty. Please try again.')
        elif not re.match("^[A-Za-z][A-Za-z0-9]*$", username):
            print('Name has to start with alphabetic characters and can contain only letters and numbers')
        elif username == "Computer":
            print('Name cannot be "Computer". Please try again.')
        elif len(username) > 20:
            print('Name cannot be longer than 20 characters. Please try again.')
        else: return username

def main():
    clear_terminal()
    display_instructions()
    clear_terminal()

    print(f'\nWelcome to this little memory game.\n')
    player1.name = name_input()

    print(f'\nHello {player1.name}! \u2665 You get the first turn', end = '', flush = True)
    time.sleep(0.7)
    print('.', end = '', flush = True)
    time.sleep(0.7)
    print('.', end = '', flush = True)
    time.sleep(0.7)
    print('.', end = '', flush = True)
    time.sleep(0.7)

    while not end_of_game():
        active_player = player1 if player1.active else player2
        draw_board(board, active_player)
        player_turn(active_player)
        
        
    
    
    

main()