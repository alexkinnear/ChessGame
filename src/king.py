from piece import Piece
from util import in_bounds, is_empty, is_enemy


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.value = 100

    def __repr__(self):
        if self.color:
            return u"\u2654"
        return u"\u265A"

    def get_pos_value(self):
        position_values = [
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
            [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
            [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
        ]
        return position_values[self.row][self.col]

    def get_moves(self, board):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if in_bounds(self.row + i, self.col + j) and (is_empty(board, self.row + i, self.col + j) or is_enemy(board, self.row + i, self.col + j, self.color)):
                    moves.append((self.row + i, self.col + j))
        return moves

    def get_img(self):
        if self.color:
            return 'img/white_king.png'
        return 'img/black_king.png'

