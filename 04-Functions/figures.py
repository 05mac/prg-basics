import turtle

window = turtle.Screen()


def draw_square(length):
    # Tworzymy żółwia "lokalnie" wewnątrz funkcji
    
    # Rysujemy kwadrat
    for i in range(4):
        pen.forward(length)
        pen.right(90)

    pen.hideturtle()
    pen.penup()


def draw_trangle(length):
    
    for i in range(3):
        pen.forward(length)
        pen.left(120)
    pen.hideturtle()
    pen.penup()    


def draw_rectangle(length_a, length_b):
 
    
   

    for i in range(4):

        if i == 0 or i == 2:
            pen.forward(length_a)
            pen.left(90)
        elif i == 1 or i == 3:
            pen.forward(length_b)
            pen.left(90)
    pen.penup()       
    pen.hideturtle()
    



