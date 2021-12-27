from piece import Piece
from util import in_bounds, is_empty, is_enemy


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.value = 30

    def __repr__(self):
        if self.color:
            return u"\u2657"
        return u"\u265D"

    def get_pos_value(self):
        position_values = [
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
            [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
            [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
            [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
            [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
            [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
            [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
        ]
        return position_values[self.row][self.col]


    def get_moves(self, board):
        moves = []
        i = 1
        # check up/left
        while in_bounds(self.row - i, self.col - i) and is_empty(board, self.row - i, self.col - i):
            moves.append((self.row - i, self.col - i))
            i += 1
        if in_bounds(self.row - i, self.col - i) and is_enemy(board, self.row - i, self.col - i, self.color):
            moves.append((self.row - i, self.col - i))
        i = 1
        # check down/left
        while in_bounds(self.row + i, self.col - i) and is_empty(board, self.row + i, self.col - i):
            moves.append((self.row + i, self.col - i))
            i += 1
        if in_bounds(self.row + i, self.col - i) and is_enemy(board, self.row + i, self.col - i, self.color):
            moves.append((self.row + i, self.col - i))
        i = 1
        # check up/right
        while in_bounds(self.row - i, self.col + i) and is_empty(board, self.row - i, self.col + i):
            moves.append((self.row - i, self.col + i))
            i += 1
        if in_bounds(self.row - i, self.col + i) and is_enemy(board, self.row - i, self.col + i, self.color):
            moves.append((self.row - i, self.col + i))
        i = 1
        # check down/left
        while in_bounds(self.row + i, self.col + i) and is_empty(board, self.row + i, self.col + i):
            moves.append((self.row + i, self.col + i))
            i += 1
        if in_bounds(self.row + i, self.col + i) and is_enemy(board, self.row + i, self.col + i, self.color):
            moves.append((self.row + i, self.col + i))
        return moves

    def get_img(self):
        if self.color:
            return 'img/white_bishop.png'
        return 'img/black_bishop.png'
