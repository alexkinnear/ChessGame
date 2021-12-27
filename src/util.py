from empty import Empty


def is_empty(board, row, col):
    return isinstance(board[row][col], Empty)


def in_bounds(row, col):
    return 0 <= row <= 7 and 0 <= col <= 7


def is_enemy(board, row, col, color):
    return board[row][col].color != color and not isinstance(board[row][col], Empty)
