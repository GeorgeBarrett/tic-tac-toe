import math
import random

class Player: 
    def __init__(self, letter): # letter = x or o
        self.letter = letter
    
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random square for the next go
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid sqaure. Try again!')
        
        return value