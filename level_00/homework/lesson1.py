from turtle import *


#we want draw a house


speed(15)
width(5)
color("grey")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#end of square

#drawing a door
forward(70)
color("black")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()



#end of door

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end
penup()
goto(185,185)
pendown()
color("black")
begin_fill()
left(30)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(60,185)
pendown()
begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


penup()
goto(170,250)
pendown()
color("brown")
begin_fill()
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(88)
end_fill()

#endhouse

penup()
goto(0, -50)
pendown()
color("green")
begin_fill()
right(90)
forward(180)
right(90)
forward(45)
right(90)
forward(550)
right(90)
forward(45)
right(90)
forward(380)
end_fill()









exitonclick()