import pygame
from .constants import BLACK, ROWS, COLS, GREEN, SQUARE_SIZE, RED, WHITE
from .Piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = 12
        self.white_left = 12
        self.red_kings = 0
        self.white_kings = 0
        self.create_board()

    def draw_cubes(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, GREEN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[row][col], self.board[piece.row][piece.col] = self.board[piece.row][piece.col], self.board[row][col]
        piece.move(row, col)

        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_cubes(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.row + 1
        row = piece.row

        if piece.color == RED or piece.king:
            pass

        if piece.color == WHITE or piece.king:
            pass

    def _traverse_left(self):
        pass

    def _traverse_right(self):
        pass
