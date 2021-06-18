from .constants import RED, WHITE, SQUARE_SIZE


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0

        if color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.calculate_position()

    def calculate_position(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True


