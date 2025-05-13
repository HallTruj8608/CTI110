import turtle


t = turtle.Turtle()
t.pensize(5)
t.color("purple")


t.penup()
t.goto(-100, 0)  
t.pendown()

t.forward(50)      
t.backward(25)     
t.right(90)
t.forward(80)      
t.left(90)
t.backward(25)      

t.penup()
t.goto(50, 0)      
t.setheading(0)
t.pendown()


t.forward(60)      
t.backward(30)     
t.right(90)
t.forward(80)      

turtle.done()
