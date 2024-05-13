
# our card symbols
heart = '\u2665'
star = '\u2605'
music = '\u266b'
sun = '\u2600'
cloud = '\u2601'
umbrella = '\u2602'
soccer_ball = '\u26bd'
basketball = '\U0001F3C0'

def initialize_board():
    board = [
        [heart, heart, star, star],
        [music, music, sun, sun],
        [cloud, cloud, umbrella, umbrella],
        [soccer_ball,soccer_ball, basketball, basketball]
    ]
    return board


def draw_board(board, card1 = None, card2 = None):
   # for col in range(len(board)) 
    print(' '* 4 + 'A' + ' ' * 4 + 'B' + ' ' * 4 + 'C' + ' ' * 4 + 'D\n')
    for x in range(len(board)):
        print('\n')
        for y in range(len(board[0])):
            print(board[x][y], end = '    ')
    print('\n')

def validate_input(pick):
    return True

def pick_card(player):
    while True:
        print('Please pick a card with a Letter and a Number')
        print('for example: A,1 ')
        pick_str = input('your pick: ')
        pick_ls = pick_str.split(',')
        if validate_input(pick_ls):
            break
    return pick_ls 

def check_pair(card1, card2):
    pass


def display_scores():
    pass
def display_final_score():
    pass

def main():
    print('-' * 40)
    username = input('Please tell me your name: \n')
    print(f'\nHello {username}! \u2665 Welcome to this little memory game.')
    # print(heart, star, music, sun, cloud, umbrella, soccer_ball, basketball)
    print('-' * 40 + '\n')

    board = initialize_board()
    draw_board(board)
    print(pick_card(username))
    
    


main()