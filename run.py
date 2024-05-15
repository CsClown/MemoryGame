import os
import time
import random

# our card symbols
heart = '\u2665'
star = '\u2605'
music = '\u266b'
sun = '\u2600'
cloud = '\u2601'
umbrella = '\u2602'
soccer_ball = '\u26bd'
basketball = '\U0001F3C0'
joker = '\U0001F0CF'

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

def initialize_board(size = 4):
    board = [
        [heart, heart, star, star],
        [music, music, sun, sun],
        [cloud, cloud, umbrella, umbrella],
        [soccer_ball,soccer_ball, basketball, basketball]
    ]
    return board

board = initialize_board()

def draw_board(board, player, pick1 = None, pick2 = None):
    """
    Draw the board depending on game state
    with either one, two or no card revealed
    """
    clear_terminal()
    if (player.name != 'Computer'):
        print(f"+++ It's your turn, {player.name}! +++")
        print(f"--- Current score: {player.score} ---")
        if player.pairs != []:
            print('Your stash:', end = " ") 
            for i in range(len(player.pairs)):
                print(player.pairs[i], end = " ")
            print('\n')
    else: 
        print("Computer's turn!")
        print(f"Current score: {player.score}")
        if player.pairs != []:
            print('Computers stash:', end = " ")
            for i in range(len(player.pairs)):
                print(player.pairs[i], end = " ")
            print('\n')
    print('\n' + '-' * 30 )
    print(' '* 5 + 'A' + ' ' * 5 + 'B' + ' ' * 5 + 'C' + ' ' * 5 + 'D')
    for x in range(len(board)):
        print(f'\n\n{x}    ', end = '')
        
        for y in range(len(board[0])):
            if board[x][y] == '0':
                print('  ', end = '    ')
            elif pick1 and pick1 == [y,x]:
                print(board[x][y], end = '    ')
            elif pick2 and pick2 == [y,x]:
                print(board[x][y], end = '    ')
            else: print(joker, end = '    ')
    print('\n' + '-' * 30 )
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
        print('*' * 40)
        print(f'Invalid data: {e}, please try again\n')
        print('*' * 40)
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
        print('+++ You got a pair!! +++')
        print(f"+++ {symbol}{symbol} +++")
        print('You get another turn!')
    else: 
        player.active = False
        if player.name == "Computer":
            player1.active = True
        else: player2.active = True
        clear_terminal()
        print('sorry no pair. its your opponents turn now', flush = True)
        time.sleep(1)
    player.pick1 = []
    player.pick2 = []

    enter = input('Press "ENTER" to continue..')
    if enter == '':
        pass
    else: print('Invalid input. Please press "Enter" to continue.')


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
                # draw_board(board, player.pick1)
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
        print('no pair, sorry')
        return False

def remove_pair(symbol):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == symbol:
                board[x][y] = '0'
    
    


def display_scores():
    pass

def display_final_score():
    pass

def main():
    
    clear_terminal()
    print('.' * 10 + 'MEMORY GAME' + '.' * 10)
    print(f'\nWelcome to this little memory game.')
    player1.name = input('Please tell me your name: ')
    clear_terminal()
    
    
    
    print(f'\nHello {player1.name}! \u2665 you get the first turn', end = '', flush = True)
    time.sleep(0.7)
    print('.', end = '', flush = True)
    time.sleep(0.7)
    print('.', end = '', flush = True)
    time.sleep(0.7)
    print('.', end = '', flush = True)
    time.sleep(0.7)
    
    
    
    while True:
        if player1.score + player2.score == 8:
            break
        else: 
            active_player = player1 if player1.active else player2
            draw_board(board, active_player)
            player_turn(active_player)
            
        
    
    
    

main()