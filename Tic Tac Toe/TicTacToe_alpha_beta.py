import time
class TicTacToe:
    def __init__(self):
        self.start_game()

    def start_game(self):
        self.game = [['-','-','-'],
                     ['-','-','-'],
                     ['-','-','-']]
        self.player = 'X'

    def print_game(self):
        print(self.game[0][0] + ' | ' + self.game[0][1] + ' | ' + self.game[0][2])
        print(self.game[1][0] + ' | ' + self.game[1][1] + ' | ' + self.game[1][2])
        print(self.game[2][0] + ' | ' + self.game[2][1] + ' | ' + self.game[2][2])
        print(' ')

    def is_valid_move(self, row, col):
        if row in range(3):
            if col in range(3):
                if self.game[row][col] == '-':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def is_game_ended(self):
        for i in range(0, 3):
            if (self.game[0][i] != '-' and self.game[0][i] == self.game[1][i] and self.game[1][i] == self.game[2][i]):
                return self.game[0][i]
        for i in range(0, 3):
            if (self.game[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.game[i] == ['O', 'O', 'O']):
                return 'O'
        if self.game[0][0] != '-' and self.game[0][0] == self.game[1][1] and self.game[0][0] == self.game[2][2]:
            return self.game[1][1]
        if self.game[0][2] != '-' and self.game[0][2] == self.game[1][1] and self.game[1][1] == self.game[2][0]:
            return self.game[1][1]
        for row in range(0, 3):
            for col in range(0, 3):
                if self.game[row][col] == '-':
                    return None
        return '-'

    def maxAI_AlphaBeta(self, a, b):
        max_score = -2
        row = None
        col = None

        result = self.is_game_ended()

        if result == 'X':
            return (-1, 0, 0)
        elif result == '-':
            return (0, 0, 0)
        elif result == 'O':
            return (1, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.game[i][j] == '-':
                    self.game[i][j] = 'O'
                    (m, min_i, min_j) = self.minHUMAN_AlphaBeta(a, b)
                    if m > max_score:
                        max_score = m
                        row = i
                        col = j
                    self.game[i][j] = '-'
                    if max_score >= b:
                        return (max_score, row, col)

                    if max_score > a:
                        a = max_score
        return (max_score, row, col)

    def minHUMAN_AlphaBeta(self, a, b):

        min_score = 2

        row = None
        col = None

        result = self.is_game_ended()

        if result == 'X':
            return (-1, 0, 0)
        elif result == '-':
            return (0, 0, 0)
        elif result == 'O':
            return (1, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.game[i][j] == '-':
                    self.game[i][j] = 'X'
                    (m, max_i, max_j) = self.maxAI_AlphaBeta(a, b)
                    if m < min_score:
                        min_score = m
                        row = i
                        col = j
                    self.game[i][j] = '-'

                    if min_score <= a:
                        return (min_score, row, col)

                    if min_score < b:
                        b = min_score
        return (min_score, row, col)

    def play_game(self):    
        while True:
            self.print_game()
            self.result = self.is_game_ended()

            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")


                self.start_game()
                return

            if self.player == 'X':

                while True:
                    start = time.time()
                    (m, qx, qy) = self.minHUMAN_AlphaBeta(-2, 2)
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    row = int(input('Insert Row: '))
                    col = int(input('Insert Column: '))

                    (qx, qy) = (row, col)

                    if self.is_valid_move(row, col):
                        self.game[row][col] = 'X'
                        self.player = 'O'
                        break
                    else:
                        print('Invalid Move')

            else:
                (m, row, col) = self.maxAI_AlphaBeta(-2, 2)
                self.game[row][col] = 'O'
                self.player = 'X'

tic_tac_toe = TicTacToe()
tic_tac_toe.play_game()