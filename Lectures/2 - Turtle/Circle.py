# turtle

import turtle
import keyboard

turtle.shape('turtle')
turtle.speed(1)

while keyboard.is_pressed("Esc") == False :
    turtle.forward(5)
    turtle.left(4)  