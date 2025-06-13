from turtle import*

#we want to paint a house

#step 1: draw as square
speed(5)
width(5)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawind a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


color("purple")
begin_fill()
left(30)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(60)
end_fill()

penup()
goto(200,200)
pendown()

begin_fill()
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(60)
end_fill()















exitonclick()
