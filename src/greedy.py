from copy import deepcopy
from collections import defaultdict
from empty import Empty


def get_white_value(white):
    score = 0
    for piece in white:
        score += piece.value
    return score


def get_black_value(black):
    score = 0
    for piece in black:
        score += piece.value
    return score


def get_black_score(board, black, white):  # color is True for white score and False for black score
    black_pieces_score = get_black_value(black)
    white_pieces_score = get_white_value(white)

    score = black_pieces_score - white_pieces_score
    for i in range(8):
        for j in range(8):
            if not board[i][j].color:
                score += board[i][j].get_pos_value()
            elif board[i][j].color:
                score -= board[i][j].get_pos_value()
    return score


def get_all_moves(board, color):
    moves = defaultdict(list)
    for i in range(8):
        for j in range(8):
            if board[i][j].color == color:
                moves[(i, j)].append(board[i][j].get_moves(board))
    return moves


def make_move(board, black, white, from_pos, to_pos):
    captured = board[to_pos[0]][to_pos[1]]
    if board[from_pos[0]][from_pos[0]].color:
        if captured in black:
            black.remove(captured)
    else:
        if captured in white:
            white.remove(captured)

    board[to_pos[0]][to_pos[1]] = board[from_pos[0]][from_pos[1]]
    board[to_pos[0]][to_pos[1]].row = to_pos[0]
    board[to_pos[0]][to_pos[1]].col = to_pos[1]
    board[from_pos[0]][from_pos[1]] = Empty(from_pos[0], from_pos[1])
    return board, black, white


def greedy(board, color, black, white):  # color is True for white score and False for black score
    moves = get_all_moves(board, color)
    scores = {}
    for from_pos in moves:
        for move in moves[from_pos]:
            for to_pos in move:
                b, bl, wh = make_move(deepcopy(board), deepcopy(black), deepcopy(white), from_pos, to_pos)
                scores[(from_pos, to_pos)] = get_black_score(b, bl, wh)

    k = list(scores.keys())
    v = list(scores.values())
    if color:
        return k[v.index(min(v))]
    return k[v.index(max(v))]
