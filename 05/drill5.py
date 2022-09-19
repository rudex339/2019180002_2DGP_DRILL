import turtle

def move_xp():
    
    turtle.setheading(0)  

    turtle.forward(100)
    turtle.stamp()
def move_xm():
    
    turtle.setheading(180)  

    turtle.forward(100)
    turtle.stamp()
def move_yp():
    
    turtle.setheading(90)  

    turtle.forward(100)
    turtle.stamp()
def move_ym():
    
    turtle.setheading(270)  

    turtle.forward(100)
    turtle.stamp()
def restart():
    turtle.reset()
turtle.shape('turtle')
turtle.onkey(move_xp,'d')
turtle.onkey(move_xm,'a')
turtle.onkey(move_yp,'w')
turtle.onkey(move_ym,'s')
turtle.onkey(restart,'Escape')
turtle.listen()
    
