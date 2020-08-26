Game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

#X is human
#O is AI

def print_game(game):
    print(game[0][0] + ' | ' + game[0][1] + ' | ' + game[0][2])
    print(game[1][0] + ' | ' + game[1][1] + ' | ' + game[1][2])
    print(game[2][0] + ' | ' + game[2][1] + ' | ' + game[2][2])

def get_coordinates(position):
    return [int((position)/3), (position)%3]

def is_valid_move(game, position):
    if position in range(9):
        row, col = get_coordinates(position)
        if game[row][col] == '-':
            return True
    else:
        return False
            
def is_game_ended(game):
    #2 conditions: either player wins or game tied
    for i in range(3):
        #horizontal win
        if game[i] == ['X','X','X']:
            return ['yes','X']
        if game[i] == ['O','O','O']:
            return ['yes','O']
        
        #vertical win
        if game[0][i] != '-' and game[0][i] == game[1][i] and game[1][i] == game[2][i]:
            return ['yes', game[0][i]]
    
    #1st diagonal win
    if game[0][0] != '-' and game[0][0] == game[1][1] and game[1][1] == game[2][2]:
        return ['yes', game[1][1]]

    #2nd diagonal win
    if game[0][2] != '-' and game[0][2] == game[1][1] and game[1][1] == game[2][0]:
        return ['yes', game[1][1]]

    #is tie
    for i in range(3):
        for j in range(3):
            if game[i][j] == '-':
                return ['no']
    return['yes', 'tie']

# AI is max
def maxAI(game):
    score = -2
    pos = None

    result = is_game_ended(game)

    if result[0] == 'yes':
        if result[1] == 'X':
            return [-1,0]
        elif result[1] == 'tie':
            return [0,0]
        elif result[1] == 'O':
            return [1,0]

    for i in range(9):
        r,c = get_coordinates(i)
        if game[r][c] == '-':
            game[r][c] == 'O'
            [m, min_pos] = minHUMAN(game)
            #print(m,max_pos)
            if m > score:
                score = m
                pos = 3*r + c

            game[i][j] = '-'
    
    return [score, pos]

#min is human
def minHUMAN(game):
    score = 2
    pos = None

    result = is_game_ended(game)
    
    if result[0] == 'yes':
        if result[1] == 'X':
            return [-1,0]
        if result[1] == 'tie':
            return [0,0]
        if result[1] == 'O':
            return [1,0]
    
    for i in range(9):
        r,c = get_coordinates(i)
        if game[r][c] == '-':
            game[r][c] == 'X'
            [m, max_pos] = maxAI(game)
            #print(m,max_pos)
            if m < score:
                score = m
                pos = 3*r + c

            game[i][j] = '-'
    
    return [score, pos]


def start_game(Game):
    
    while True:
        
        print_game(Game)

        result = is_game_ended(Game)
        if result[0] == 'yes':
            if result[1] == 'X':
                print('Well Done!!  You Won!!')
            if result[1] == 'tie':
                print('Looks like AI is as good as you. Game Tied')
            if result[1] == 'O':
                print('You lost!! Better luck next time')
            
            
            return
        player = 'O'
        if player == 'X':
            while True:
                [score,pos] = minHUMAN(Game)
                pos1 = int(input('Insert position in range 1 - 9: ')) - 1
                pos = pos1

                if is_valid_move(Game, pos1):
                    row,col = get_coordinates(pos1)
                    Game[row][col] = 'X'
                    player = 'O'
                    break
                else:
                    print('Invalid move')
        else:
            [score, pos1] = maxAI(Game)
            row1,col1 = get_coordinates(pos1)
            Game[row1][col1] = 'O'
            player = 'X'

start_game(Game)