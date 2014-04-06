"""
We are going to write a project that does chess-related
computation. The project is split into several parts.

Write tests for appropriate functions in a separate file
chess_spec.py.

Part 1.
a) Create a class called Piece that has two members -
piece and color. piece will be "K", "Q", "R", "B",
"N", and "P." color will be "w" or "b."

b) Write a function called show_piece that takes a Piece
and returns the string concatenation of the piece and the
color. For instance, a black king should be printed as
"Kb."

c) Write a function called prettify that takes in
an 8x8 tuple of tuples, and returns a string that, when
printed, will display the board in a human-readable way.
Note that this prettify function returns a string, it
DOES NOT print anything.

  
The prettify function should use whitespace if the value
at an index is None. Otherwise, we can assume it is a Piece
and we use the show_piece string associated with it.

d) Write a function called pretty_print that takes in
an 8x8 tuple of tuples, and actually prints out the prettified
form of the board to the screen.

e) Implement a function called fresh_board that returns
an 8x8 tuple of tuples, where each square is either a
Piece or None. None represents a square with no piece on it.
The board returned should be initialized to the proper starting
chess position state.


p = Piece('K', 'b')
print p.show_piece() # 'Kb'
"""
import sys
import os

class ChessException(Exception):

    def __init__(self, value):

        self.parameter = value

    def __str__(self):

        return repr(self.parameter)

def raise_piece_not_recongized_exception():

    raise ChessException("Piece not recongized!")

def raise_piece_invalid_move_exception():

    raise ChessException("Piece move is invalid!")

class Piece():
    def __init__(self, piece, color):
        if piece not in 'KQBNP' or color not in 'wb':
            raise_piece_not_recongized_exception
        self.piece = piece
        self.color = color
        
    def show_piece(self):
        return self.piece + self.color
    
class Board():
    def __init__(self, board = None):
        if board == None: 
            white_king = Piece('K','w')
            white_rook = Piece('R','w')
            white_queen = Piece('Q','w')
            white_bishop = Piece('B','w')
            white_knight = Piece('N','w')
            white_pawn = Piece('P','w')
            
            black_king = Piece('K','b')
            black_rook = Piece('R','b')
            black_queen = Piece('Q','b')
            black_bishop = Piece('B','b')
            black_knight = Piece('N','b')
            black_pawn = Piece('P','b')
            
            self.board = {i + j: None for i in 'ABCDEFGH' for j in '87654321'}
            
            self.board['A1'] =  white_rook
            self.board['B1'] =  white_knight
            self.board['C1'] =  white_bishop
            self.board['D1'] =  white_king
            self.board['E1'] =  white_queen
            self.board['F1'] =  white_bishop
            self.board['G1'] =  white_knight
            self.board['H1'] =  white_rook
            self.board['A2'] =  white_pawn
            self.board['B2'] =  white_pawn
            self.board['C2'] =  white_pawn
            self.board['D2'] =  white_pawn
            self.board['E2'] =  white_pawn
            self.board['F2'] =  white_pawn
            self.board['G2'] =  white_pawn
            self.board['H2'] =  white_pawn
        
            self.board['A8'] =  black_rook
            self.board['B8'] =  black_knight
            self.board['C8'] =  black_bishop
            self.board['D8'] =  black_king
            self.board['E8'] =  black_queen
            self.board['F8'] =  black_bishop
            self.board['G8'] =  black_knight
            self.board['H8'] =  black_rook
            self.board['A7'] =  black_pawn
            self.board['B7'] =  black_pawn
            self.board['C7'] =  black_pawn
            self.board['D7'] =  black_pawn
            self.board['E7'] =  black_pawn
            self.board['F7'] =  black_pawn
            self.board['G7'] =  black_pawn
            self.board['H7'] =  black_pawn
        else:
            self.board = board
    
    def prettify(self):
        
        return '\n'.join([(' '.join(['  ' if not self.board[x] else self.board[x].show_piece() for x in [y+z for y in 'ABCDEFGH']])) for z in '87654321'])
        

    def pretty_print(self):
        print self.prettify()
    
    def move(self, start, end):
        start = start.upper()
        end = end.upper()
        if start not in self.board.keys(): raise_piece_invalid_move_exception
        if end not in self.board.keys(): raise_piece_invalid_move_exception
        if not self.board[start]: raise_piece_invalid_move_exception
        if  not self.board[end] and not self.board[start]:
            if self.board[start].show_piece()[1] == self.board[end].show_piece()[1]: raise_piece_invalid_move_exception
        self.board[start], self.board[end] = None, self.board[start]
        return Board( {i + j: None if not self.board[i+j] else self.board[i+j] for i in 'ABCDEFGH' for j in '87654321' })
        
        
#a = Board()
#a.pretty_print()
#b = a.move('e2', 'E4').move('H8', 'h6').move('A2', 'A3')
#b.pretty_print()
def read_and_move(l):
    
    #board = board.move(l[0][0], l[0][1])

    #previous_move, current_move, next_move = l[0], l[1], l[2:]
    
    def move_piece(board, index, l):
        if len(l) == index+1:
            os.system('clear')
            board = board.move(l[index][0], l[index][1])
            board.pretty_print()
            print "end of game! "
            user_input=raw_input("next? B)ack, E)nd....  ")
            if user_input[0] == 'E':
                sys.exit("Program ended")
            elif user_input[0] == 'B':
                board = board.move(l[index][1], l[index][0])
                board = board.move(l[index-1][1], l[index-1][0])
                return move_piece(board, index - 1, l)
            else:
                board = board.move(l[index][1], l[index][0])
                return move_piece(board, index, l)
            return
        else:
            os.system('clear')
            #board = board.move(l[0][0], l[0][1])
            board.pretty_print()
            print
            if index == 0:
                board = board.move(l[index][0], l[index][1])
                os.system('clear')
                board.pretty_print()
                user_input=raw_input("next? N)ext, E)nd.....  ")
                if user_input[0] == 'E':
                    sys.exit("Program ended")
                elif user_input[0] == 'N':
                    return move_piece(board, index + 1, l)
                else: return move_piece(board.move(l[index][1], l[index][0]), index, l)
            else:
                
                board = board.move(l[index][0], l[index][1])
                os.system('clear')
                board.pretty_print()
                user_input=raw_input("next? B)ack N)ext, E)nd....  ")
                if user_input[0] == 'E':
                    sys.exit("Program ended")
                elif user_input[0] == 'N':
                    return move_piece(board,index + 1, l)
                elif user_input[0] == 'B':
                    board = board.move(l[index][1], l[index][0])
                    board = board.move(l[index-1][1], l[index-1][0])
                    return move_piece(board, index - 1, l)
                else:
                    board = board.move(l[index][1], l[index][0])
                    return move_piece(board, index, l)
    os.system('clear')
    board = Board()
    #board.pretty_print()
    move_piece(board, 0, l)
    

def read_file(s):

    try:
        with open(s, 'r') as infile:
            move = [tuple(line.split()) for line in infile]
        return move
    except IOError:
        
        sys.exit("The file %s cannot be found, exiting gracefully" % s)

def main(s):
    chess_move_list = read_file(s)
    
    print  chess_move_list
    read_and_move(chess_move_list)


if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        
        sys.exit("Usage: python %s [input file path]" % sys.argv[0])
           
    read_in_file_name = sys.argv[1]
    main(read_in_file_name)

        
      