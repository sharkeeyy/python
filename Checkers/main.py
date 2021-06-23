import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_coordinates_from_mouse_click(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_coordinates_from_mouse_click(position)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
