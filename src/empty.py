from piece import Piece


class Empty(Piece):

    def __init__(self, row, col):
        super().__init__(row, col, None)
        self.value = 0

    def __repr__(self):
        return ' '

    def get_pos_value(self):
        return 0.0

    def get_moves(self, board):
        return []

    def get_img(self):
        return 'img/empty.png'
