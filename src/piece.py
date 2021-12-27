from abc import abstractmethod


class Piece:
    row: int
    col: int
    color: bool  # True for white, False for black

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    @abstractmethod
    def get_pos_value(self):
        pass

    @abstractmethod
    def get_moves(self, board):
        pass

    @abstractmethod
    def get_img(self):
        pass
