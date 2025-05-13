import turtle

t = turtle.Turtle()
t.pensize(3)
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-150, -150)
t.pendown()

sides = 0
while sides < 3:
    t.forward(100)
    t.left(120)
    sides += 1

turtle.done()
