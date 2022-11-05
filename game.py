class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # I will use a single list to rep a 3x3 board
        self.current_winner = None # to keep track of the champion

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # getting rows
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        
        #I commented this code out as I can condense it
        # moves = []
        # for (i, square) in enumerate(self.board):
        #     if square == '':
        #         moves.append(i)
        
        # return moves

        return [i for i, square in enumerate(self.board) if square == ' ']
