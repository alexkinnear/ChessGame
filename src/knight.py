from piece import Piece
from util import in_bounds, is_empty, is_enemy


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.value = 20

    def __repr__(self):
        if self.color:
            return u"\u2658"
        return u"\u265E"

    def get_pos_value(self):
        position_values = [
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
            [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
            [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
            [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
            [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
            [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
            [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
        ]
        return position_values[self.row][self.col]

    def get_moves(self, board):
        moves = []
        # Down 2, right 1
        if in_bounds(self.row + 2, self.col + 1) and (
                is_empty(board, self.row + 2, self.col + 1) or is_enemy(board, self.row + 2, self.col + 1, self.color)):
            moves.append((self.row + 2, self.col + 1))
        # Down 2, left 1
        if in_bounds(self.row + 2, self.col - 1) and (
                is_empty(board, self.row + 2, self.col - 1) or is_enemy(board, self.row + 2, self.col - 1, self.color)):
            moves.append((self.row + 2, self.col - 1))
        # Down 1, right 2
        if in_bounds(self.row + 1, self.col + 2) and (
                is_empty(board, self.row + 1, self.col + 2) or is_enemy(board, self.row + 1, self.col + 2, self.color)):
            moves.append((self.row + 1, self.col + 2))
        # Down 1, left 2
        if in_bounds(self.row + 1, self.col - 2) and (
                is_empty(board, self.row + 1, self.col - 2) or is_enemy(board, self.row + 1, self.col - 2, self.color)):
            moves.append((self.row + 1, self.col - 2))
        # Up 2, right 1
        if in_bounds(self.row - 2, self.col + 1) and (
                is_empty(board, self.row - 2, self.col + 1) or is_enemy(board, self.row - 2, self.col + 1, self.color)):
            moves.append((self.row - 2, self.col + 1))
        # Up 2, left 1
        if in_bounds(self.row - 2, self.col - 1) and (
                is_empty(board, self.row - 2, self.col - 1) or is_enemy(board, self.row - 2, self.col - 1, self.color)):
            moves.append((self.row - 2, self.col - 1))
        # Up 1, right 2
        if in_bounds(self.row - 1, self.col + 2) and (
                is_empty(board, self.row - 1, self.col + 2) or is_enemy(board, self.row - 1, self.col + 2, self.color)):
            moves.append((self.row - 1, self.col + 2))
        # Down 1, left 2
        if in_bounds(self.row - 1, self.col - 2) and (
                is_empty(board, self.row - 1, self.col - 2) or is_enemy(board, self.row - 1, self.col - 2, self.color)):
            moves.append((self.row - 1, self.col - 2))
        return moves

    def get_img(self):
        if self.color:
            return 'img/white_knight.png'
        return 'img/black_knight.png'
