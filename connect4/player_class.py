#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    """ a data type for a Connect Four player"""
    def __init__(self,checker):
        """a constructor for player objects"""
        assert(checker=='X' or checker=='O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """returns a string representation of player object"""
        s = 'Player ' + self.checker
        return s
    def opponent_checker(self):
        """ returns the opponent checker"""
        if  self.checker == 'X':
            return 'O'
        else:
            return 'X'
    def next_move(self, b):
        """ accepts a Board object b as a parameter
            and returns the column where the player
            wants to make the next move
        """
        self.num_moves += 1

        while True:
            col = input('Enter a column: ')
            if col in "0123456":
                coln = int(col)
                if b.can_add_to(coln):
                    return coln
            print('Try again!')

            
