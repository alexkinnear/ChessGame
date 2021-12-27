from piece import Piece
from rook import Rook
from bishop import Bishop


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.value = 90

    def __repr__(self):
        if self.color:
            return u"\u2655"
        return u"\u265B"

    def get_pos_value(self):
        position_values = [
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
            [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
            [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
            [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
            [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
            [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
        ]
        return position_values[self.row][self.col]

    def get_moves(self, board):
        moves = Rook(self.row, self.col, self.color).get_moves(board)
        moves.extend(Bishop(self.row, self.col, self.color).get_moves(board))
        return moves

    def get_img(self):
        if self.color:
            return 'img/white_queen.png'
        return 'img/black_queen.png'
