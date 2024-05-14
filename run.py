import os

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

row_labels = ['A','B','C','D']


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

# class pick:
#     def __init__(self, card1, card2)

# class game_board:
#     def __init__(self, size)
#         self.size = size
#         self.board = []

#     def ini

def clear_terminal():
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

def draw_board(board, pick1 = None, pick2 = None):
    """
    Draw the board depending on game state
    with either one, two or no card revealed
    """
    clear_terminal()
    print('\n' + '-' * 30 )
    print(' '* 5 + 'A' + ' ' * 5 + 'B' + ' ' * 5 + 'C' + ' ' * 5 + 'D')
    for x in range(len(board)):
        print(f'\n\n{x}    ', end = '')
        
        for y in range(len(board[0])):
            if pick1 and pick1 == [y,x]:
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
        elif pick[0].upper() not in row_labels:
            raise ValueError(
                f'Please pick a letter A - D, you provided "{pick[0].upper()}"'
            )
    except ValueError as e:
        print('*' * 40)
        print(f'Invalid data: {e}, please try again\n')
        return False
    else: return True
def player_turn(player):
    """
    Facilitates a whole turn of the active player
    """
    # while True:
    #     if card1:
    #         if card2:
    #     else
    #         card1 = pick_card()        
    #         card2 = pick_card
    pass


def pick_card(player):
    """
    User Input for choosing a card on the board
    calls validate_input for input validation ;)
    returns list
    """
    

    while True:
        if player.pick1 == []:
            print('+++ Please pick your FIRST card! Example: A1 +++')
            
            pick_str = input('+++ YOUR PICK: ')
            pick_strip = [i.strip() for i in pick_str]
            pick_ls = [string for string in pick_strip]
            if validate_input(pick_strip):
                player.pick1 = [pick_strip[0].upper(),int(pick_strip[1])]
                # draw_board(board, player.pick1)
                print(f'You chose: {player.pick1[0]}{player.pick1[1]}')
                card1 = [ord(player.pick1[0]) - 65, player.pick1[1]]
                draw_board(board, card1)
        elif player.pick2 == []:
            print('+++ Please pick your SECOND card! Example: A1 +++')
            
            pick_str = input('+++ YOUR PICK: ')
            pick_strip = [i.strip() for i in pick_str]
            pick_ls = [string for string in pick_strip]
            if validate_input(pick_strip):
                player.pick2 = [pick_strip[0].upper(),int(pick_strip[1])]
                if player.pick2 == player.pick1:
                    print('+++ You cannot chose the same card twice! +++')
                    player.pick2 = []
                    continue
                print(f'You chose: {player.pick2[0]}{player.pick2[1]}')
                card2 = [ord(player.pick2[0]) - 65, player.pick2[1]]
                draw_board(board, card1, card2)
                break
    return

def check_pair(card1, card2):
    if card1 == card2:
        print('+++ You got a pair!! +++')
        return True
    else: return False

def remove_pair(card1, card2):
    pass


def display_scores():
    pass

def display_final_score():
    pass

def main():
    
    print('-' * 40)
    username = input('Please tell me your name: \n')
    print(f'\nHello {username}! \u2665 Welcome to this little memory game.')
    print('-' * 40 + '\n')
    
    player1 = player(username)
    player2 = player('computer')
    player2.active = False
    active_player = player1
    
    card1 = None
    card2 = None

    
    
    
    
    yes = pick_card(active_player)
    
    


main()