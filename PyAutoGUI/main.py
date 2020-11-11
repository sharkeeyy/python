import pyautogui as pg
import keyboard
import time
import random

keyboard.wait('+')

while not keyboard.is_pressed("Esc"):
    x = random.randint(200, 800)
    y = random.randint(200, 600)
    pg.moveTo(x, y)
    pg.mouseDown(button='left')
    x = random.randint(200, 800)
    y = random.randint(200, 600)
    pg.moveTo(x, y)
    pg.mouseUp()


