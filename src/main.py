from chessboard import start_board
from game import Chess

if __name__ == "__main__":
    board = start_board()
    game = Chess(board)
    game.play()
