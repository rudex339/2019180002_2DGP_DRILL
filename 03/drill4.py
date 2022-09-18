import turtle

count =0

while (count<6):
    turtle.penup(); turtle.goto(0,100*count);turtle.pendown()
    turtle.forward(500)
    count = count+1
count =0
turtle.penup();turtle.home();turtle.pendown();turtle.left(90); 
while (count<6):
    turtle.penup(); turtle.goto(100*count,0);turtle.pendown()
    turtle.forward(500)
    count = count+1
