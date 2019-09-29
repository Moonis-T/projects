#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """a more “intelligent” computer player – one that
       uses techniques from artificial intelligence (AI)
       to choose its next move.
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructor for AIPlayer
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak  == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        


    def __repr__(self):
        """returns a string representing an AIPlayer object
        """
        s = 'Player ' + str(self.checker)
        v = ' ('+ self.tiebreak+', '+str(self.lookahead)+')'
        s += v
        return s

    def max_score_column(self, scores):
        """takes a list scores containing a score for each
           column of the board, and that returns the index
           of the column with the maximum score
        """
        max_s = max(scores)
        max_i = []
        for r in range(len(scores)):
            if scores[r] == max_s:
                max_i += [r]
        max_i
        if self.tiebreak == 'LEFT':
            return max_i[0]
        elif self.tiebreak == 'RIGHT':
            return max_i[-1]
        else:
            return random.choice(max_i)

    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores
           for the columns in b
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col)==False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker())== True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak,self.lookahead-1)
                opp_scores = opp.scores_for(b)
                if max(opp_scores)==0:
                     scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                elif max(opp_scores) == 100:
                    scores[col] = 0

                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """overrides (i.e., replaces) the next_move
           method that is inherited from Player
        """
        self.num_moves += 1
        scores = AIPlayer(self.checker, self.tiebreak, self.lookahead).scores_for(b)
        best_c = self.max_score_column(scores)
        return best_c
            
        
        
        
        
        

