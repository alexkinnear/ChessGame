from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from empty import Empty


def start_board():
    return [[Rook(0, 0, False), Knight(0, 1, False), Bishop(0, 2, False), Queen(0, 3, False),
             King(0, 4, False), Bishop(0, 5, False), Knight(0, 6, False), Rook(0, 7, False)],
            [Pawn(1, i, False) for i in range(8)],
            [Empty(2, i) for i in range(8)],
            [Empty(2, i) for i in range(8)],
            [Empty(2, i) for i in range(8)],
            [Empty(2, i) for i in range(8)],
            [Pawn(6, i, True) for i in range(8)],
            [Rook(7, 0, True), Knight(7, 1, True), Bishop(7, 2, True), Queen(7, 3, True),
             King(7, 4, True), Bishop(7, 5, True), Knight(7, 6, True), Rook(7, 7, True)]]


class Board:
    def __init__(self):
        self.board = start_board()

    def display(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end='  ')
            print()
