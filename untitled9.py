"""B30 Python practical revision demo."""

from turtle import *

bgcolor("light blue")
pencolor("black")
for pair in range(2):
    fd(150)
    rt(90)
    fd(60)
    rt(90)

#circle
penup()
goto(75, 50)  # Center the circle relative to the rectangle
pendown()

pencolor("black")
fillcolor("light pink")
begin_fill()
circle(40)  # Draws a circle with a radius of 40 pixels
end_fill()
done()