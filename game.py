class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # I will use a single list to rep a 3x3 board
        self.current_winner = None # to keep track of the champion

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # getting rows
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():