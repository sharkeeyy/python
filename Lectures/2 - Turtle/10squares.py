import turtle
import keyboard

turtle.shape('turtle')
turtle.speed(1)

side = 40

for i in range (10) :
    turtle.penup()
    turtle.goto(-side, -side)
    turtle.pendown()
    
    for y in range (4) :
        turtle.forward(side*2)
        turtle.left(90)

    i += 1
    side += 10  