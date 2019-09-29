class Board:
    """ a data type for a Connect Four board with arbitary
        dimensions
    """
    def __init__(self, height, width):
        """a constructor for board objects
        """
        self.height = height
        self.width = width
        self.slots = [[' ']*width for r in range(height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

    # Add code here for the hyphens at the bottom of the board
    # and the numbers underneath it.
        for row in range(2*self.width+1):
            s += '-'
        s += '\n'

        v = 0
        for r in range(self.width):
            v = v % 10
            s += ' ' + str(v)
            v += 1
        
        return s
    def add_checker(self, checker, col):
        """ adds specified checker into the specified column
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        while self.slots[row][col] == ' ' and row < (self.height-1):
            row += 1
        if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
            self.slots[row-1][col] = checker
        else:
            self.slots[row][col] = checker

    def reset(self):
        """ resets the Board back to original state
        """
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if specified column has spots for checker
            and False otherwise
        """
        if 0 <= col < self.width:
            if self.slots[0][col] == 'X' or self.slots[0][col]== 'O':
                return False
            else:
                return True
        else:
            return False
    def is_full(self):
        """ checks if Board is full
        """
        for c in range(self.width):
            if self.can_add_to(c) == True:
                return False
        return True
    
    def remove_checker(self, col):
        """ removes topmost checker from specified column
        """
        row = 0
        while self.slots[row][col] == ' ' and row < (self.height-1):
            row += 1
        self.slots[row][col] = ' '

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        return False
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ returns True if the board has four consecutive
            spots filled with specified checker diagonally upwards
        """
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ returns True if the board has four consecutive
            spots filled with specified checker diagonally downwards
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False    
        

    def is_win_for(self, checker):
        """ returns True if the checker has four consecutive slots
            either horizontally, vertically, digonally upwards or diagonally
            downwards and False otherwise
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
        
        
