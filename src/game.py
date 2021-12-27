import pygame
from empty import Empty
from king import King
from copy import deepcopy
from time import sleep
from greedy import greedy


class Chess:
    def __init__(self, board):
        pygame.init()
        self.WHITE = (255, 255, 255)
        self.BROWN = (199, 158, 125)
        self.board = board
        self.WIDTH, self.HEIGHT = 600, 600
        self.tile_size = self.WIDTH // 8
        self.display = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.white = [piece for piece in self.board[6]]
        for piece in self.board[7]:
            self.white.append(piece)
        self.black = [piece for piece in self.board[1]]
        for piece in self.board[0]:
            self.black.append(piece)
        pygame.display.set_caption("Chess")

    def draw_board(self, moves):
        dark = True
        for row in range(0, self.WIDTH, self.tile_size):
            dark = not dark
            for col in range(0, self.HEIGHT, self.tile_size):

                # draw square
                color = self.WHITE if dark else self.BROWN
                rect = (row, col, self.tile_size, self.tile_size)
                pygame.draw.rect(self.display, color, rect)
                c, r = row // self.tile_size, col // self.tile_size

                # add pieces
                if not self.board[r][c].get_img() == 'img/empty.png':
                    img = pygame.image.load(self.board[r][c].get_img())
                    self.display.blit(img, (row, col))

                # add possible moves
                if (r, c) in moves:
                    rect = pygame.Rect(row, col, self.tile_size, self.tile_size)
                    pygame.draw.rect(self.display, (0, 255, 0), rect, 5)
                dark = not dark
        pygame.display.flip()

    def move(self, selected, new_row, new_col):
        captured = self.board[new_row][new_col]
        if self.board[selected[0]][selected[1]].color:
            if not isinstance(captured, Empty):
                self.black.remove(captured)
        else:
            if not isinstance(captured, Empty):
                self.white.remove(captured)

        self.board[new_row][new_col] = self.board[selected[0]][selected[1]]
        self.board[new_row][new_col].row = new_row
        self.board[new_row][new_col].col = new_col
        self.board[selected[0]][selected[1]] = Empty(selected[0], selected[1])

    def cpu_move(self):
        m = greedy(deepcopy(self.board), False, deepcopy(self.black), deepcopy(self.white))
        from_pos = m[0]
        to_pos = m[1]
        self.move(from_pos, to_pos[0], to_pos[1])

    def game_over(self):
        king_found = False
        for piece in self.black:
            if isinstance(piece, King):
                king_found = True
        if king_found:
            for piece in self.white:
                if isinstance(piece, King):
                    return False
            return True
        return True

    def play(self):
        playing = True
        moves = []
        selected = None
        while playing:
            for event in pygame.event.get():
                self.draw_board(moves)
                if event.type == pygame.QUIT:
                    playing = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // self.tile_size
                    col = pos[0] // self.tile_size
                    if selected is None:
                        if self.board[row][col].color:
                            moves = self.board[row][col].get_moves(self.board)
                            selected = (row, col)
                        else:
                            moves = []
                    else:
                        if (row, col) in moves:
                            self.move(selected, row, col)
                            moves = []
                            self.draw_board(moves)
                            sleep(1)
                            self.cpu_move()
                        selected = None
                if self.game_over():
                    return
