import pygame
from .board import Board
from .constants import RED, WHITE

class Game:
    def __init__(self, win):
        self.selected = None
        self.turn = RED
