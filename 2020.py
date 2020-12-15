# GNH progress wheel

from turtle import*
shape ("turtle")
speed(0)

#reset_position
def reset_position():
   setposition(0,0)

# inner line segment.
# This code will draw the shorter line segment.

COL=input("enter your color  : ")
pensize(20)
rt(90)
for i in range(6):
    color(COL)
    fd(270)
    bk(270)
    rt(60)

# this code will draw the longer line segment 
pensize(8)
lt(90)
col=input("enter your color : ")
for i in range (6):
    color(col)
    fd(350)
    bk(350)
    rt(60)

#this code will draw the inner circle
penup()
setposition(0,-70)
pendown()
begin_fill()
color("light green")
circle(70)
end_fill()
reset_position()

#this code will draw the core of the  circle
penup()
setposition(0,-60)
pendown()
begin_fill()
circle(60)
color("red")
end_fill()
reset_position()

#this code will draw the middle large circle
pensize(20)
penup()
setposition(0,-270)
pendown()
color("yellow")
circle(270)
penup()
reset_position()
pendown()

# this code is for outermost circle
penup()
setposition(0,-350)
pendown()
color(COL)
circle(350)
penup()
reset_position()
pendown()

#This code will write inner text.
color("black")
penup()
bk(50)
fd(20)
pendown()
write("GNH",font=("verdana",18,"normal"))
penup()
bk(20)
rt(90)
fd(18)
lt(90)
pendown()
write("Progress",font=("verdana",18,"normal"))
penup()
fd(15)
rt(90)
fd(20)
lt(90)
pendown()
write("wheel",font=("verdana",18,"normal"))

# writing number on the line
penup()
reset_position()
pendown()
def number():

   penup()
   fd(50)
   pendown()
   write("1")

   penup()
   fd(50)
   pendown()
   write("2")

   penup()
   fd(50)

   pendown()
   write("3")

   penup()
   fd(50)
   pendown()
   write("4")
lt(30)
for i in range(6):
      penup()
      reset_position()
      lt(60)
      fd(50)
      number()
      pendown()

#joining current rating 
penup()
reset_position()
rt(60)
fd(200)
pendown()
pensize(2)
lt(120)
fd(200)
for i in range(2):
      lt(60)
      fd(200)
lt(75)
fd(180)
lt(30)
fd(180)
lt(75)
fd(200)

#joining the target rating
bk(200)
rt(10)
fd(223)
lt(67)
fd(250)
lt(61)
fd(253)
lt(61)
fd(253)
lt(71)
fd(245)
lt(51)
fd(200)

#wording
penup()
reset_position()
fd(300)
rt(90)
fd(40)
rt(180)
pendown()

pensize(8)
write("curriculum Practice", font=("verdana",18,"normal"))
penup()
setposition(300,100)
pendown()
write("green school", font=("verdana",18,"normal"))













