from piece import Piece
from util import in_bounds, is_empty, is_enemy


class Pawn(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.value = 10

    def __repr__(self):
        if self.color:
            return u"\u2659"
        return u"\u265F"

    def get_pos_value(self):
        position_values = [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
            [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
            [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
            [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
            [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
            [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ]
        return position_values[self.row][self.col]

    def get_moves(self, board):
        moves = []
        if self.color:
            # forward 1
            if in_bounds(self.row - 1, self.col) and is_empty(board, self.row - 1, self.col):
                moves.append((self.row - 1, self.col))
            # forward 2
            if self.row == 6 and (self.row - 1, self.col) in moves and is_empty(board, self.row - 2, self.col):
                moves.append((self.row - 2, self.col))
            # attack left
            if in_bounds(self.row - 1, self.col - 1) and is_enemy(board, self.row - 1, self.col - 1, self.color):
                moves.append((self.row - 1, self.col - 1))
            # attack right
            if in_bounds(self.row - 1, self.col + 1) and is_enemy(board, self.row - 1, self.col + 1, self.color):
                moves.append((self.row - 1, self.col + 1))
        else:
            # down 1
            if in_bounds(self.row + 1, self.col) and is_empty(board, self.row + 1, self.col):
                moves.append((self.row + 1, self.col))
            # down 2
            if self.row == 1 and (self.row + 1, self.col) in moves and is_empty(board, self.row + 2, self.col):
                moves.append((self.row + 2, self.col))
            # attack left
            if in_bounds(self.row + 1, self.col - 1) and is_enemy(board, self.row + 1, self.col - 1, self.color):
                moves.append((self.row + 1, self.col - 1))
            # attack right
            if in_bounds(self.row + 1, self.col + 1) and is_enemy(board, self.row + 1, self.col + 1, self.color):
                moves.append((self.row + 1, self.col + 1))
        return moves

    def get_img(self):
        if self.color:
            return 'img/white_pawn.png'
        return 'img/black_pawn.png'



