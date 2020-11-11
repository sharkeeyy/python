import graphics as gr
import keyboard

window = gr.GraphWin(width = 800, height = 800)

def factorial_rect(A, B, C, D, deep = 10, alpha = 0.2):
    if deep == 0:
        return
    gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    A1 = ((1 - alpha) * A[0] + alpha * B[0], (1 - alpha) * A[1] + alpha * B[1])
    B1 = ((1 - alpha) * B[0] + alpha * C[0], (1 - alpha) * B[1] + alpha * C[1])
    C1 = ((1 - alpha) * C[0] + alpha * D[0], (1 - alpha) * C[1] + alpha * D[1])
    D1 = ((1 - alpha) * D[0] + alpha * A[0], (1 - alpha) * D[1] + alpha * A[1])
    factorial_rect(A1, B1, C1, D1, deep - 1)
    

factorial_rect((100, 100), (600, 100), (600, 600), (100, 600))

while keyboard.is_pressed("Esc") == False : 
    pass
  
