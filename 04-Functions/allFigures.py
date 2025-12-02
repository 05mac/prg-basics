###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures
for i in range (3):
    if i == 0:
        figures.draw_square(50)
        pen.penup()
        pen.goto(-100, 100)
    elif i == 1:
        pen.pendown()
        figures.draw_rectangle(50,25)
        pen.goto(-100, 100)
    else:
        figures.draw_trangle(30)
        pen.goto(-100, 100)
    
    



# Hide the turtle and finish
pen.hideturtle()
window.mainloop()