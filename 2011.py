from turtle import *
shape ("turtle")
speed(100)

#Bigger circle
pensize(14)
pu()
goto (0,-330)
pd()
color("yellow")
circle(330)
pu()
goto(0,0)
pd()

#Inner lines
for i in range (12):
    color("yellow")
    pensize(7)
    fd(330)
    bk(330)
    lt(30)
    pensize(17)
    color("orange")
    fd(250)
    bk(250)
    lt(30)

#position for the core circles
pu()
goto(0,-250)
pd()
circle(250)
goto(0,0)
rt(90)
fd(30)
lt(90)

#core circle 1
color("yellow")
begin_fill()
circle(30)
end_fill()

#core circle 2
pensize(11)
rt(90)
fd(10)
lt(90)
color("orange")
circle(40)

#position for stars
pu()
goto(400,150)
pd()
pensize(1)

#Draw star
def draw_star():
    for i in range(5):
        fd(35)
        rt(144)
ht()

#Target legend
color("gold")
begin_fill()
draw_star()
end_fill()
pu()
fd(45)
goto(450,130)
write("Target", font=("Verdana", 15, "normal"))

#Current rating legend
goto(400,85)
color("silver")
begin_fill()
draw_star()
end_fill()
pu()
fd(45)
goto(450,70)
write("Current Rating", font=("Verdana", 15, "normal"))

#numberline 1
goto(0,0)
def numbers(rating):
    ht()
    write(rating)
    pu()
rt(33)
num=1
for i in range(4):
        color("black")
        pu()
        fd(50)
        numbers(num)
        fd(2+i*5)
        num=num+1

#numberline 2
goto(0,0)
def numbers(rating):
    ht()
    write(rating)
    pu()
rt(57)
num=1
for i in range(4):
        color("black")
        pu()
        fd(50)
        numbers(num)
        fd(2+i*5)
        num=num+1
        
#numberline 3
goto(0,0)
def numbers(rating):
    ht()
    write(rating)
    pu()
rt(58)
num=1
for i in range(4):
        color("black")
        pu()
        fd(50)
        numbers(num)
        fd(2+i*5)
        num=num+1

#numberline 4
goto(0,0)
def numbers(rating):
    ht()
    write(rating)
    pu()
rt(60)
num=1
for i in range(4):
        color("black")
        pu()
        fd(50)
        numbers(num)
        fd(2+i*5)
        num=num+1


#numberline 5
goto(0,0)
def numbers(rating):
    ht()
    write(rating)
    pu()
rt(62)
num=1
for i in range(4):
        color("black")
        pu()
        fd(50)
        numbers(num)
        fd(2+i*5)
        num=num+1

#numberline 6
goto(0,0)
def numbers(rating):
    ht()
    write(rating)
    pu()
rt(62)
num=1
for i in range(4):
        color("black")
        pu()
        fd(50)
        numbers(num)
        fd(2+i*5)
        num=num+1


#School community_Vitality
color("black")
pu()
rt(45)
goto(-180,30)
write("School Community-Vitality", font=("Ariel", 14, "normal"), align="Right")

#Leadership and Management
color("black")
pu()
goto(140,0)
goto(140,275)
write("Leadership and Management", font=("Ariel", 14, "normal"), align="Right")

#Green School
color("black")
pu()
rt(45)
goto(350,30)
write("Green School", font=("Ariel", 14, "normal"), align="Right")

#Broader Learning
color("black")
pu()
goto(140,0)
goto(100,-290)
write("Broader Learning", font=("Ariel", 14, "normal"), align="Right")

#Holistic Assessment
color("black")
pu()
rt(45)
goto(-90,-150)
write("Holistic Assessment", font=("Ariel", 14, "normal"), align="Right")

#Curriculum Practice
color("black")
pu()
rt(45)
goto(290,-150)
write("Curriculum Practice", font=("Ariel", 14, "normal"), align="Right")

#GNH Progress Wheel
goto(0,10)
pd()
write("GNH", font=("Ariel", 13, "normal"), align="Center")
pu()
goto(0,-5)
write("Progress", font=("Ariel", 13, "normal"), align="Center")
pu()
goto(0,-25)
write("Wheel", font=("Ariel", 13, "normal"), align="Center")


goto(0,0)
rt(180)
#current rating
goto(0,-155)
pd()
size = int(input("Choose one pensize for the line:"))
pensize(size)
color("silver")
for i in range(4):
    fd(167)
    lt(62)
lt(17)
fd(145)
lt(20)
fd(130)

#target
size = int(input("Choose one pensize for the line:"))
pensize(size)
color("gold")
lt(60)
fd(180)
lt(73)    
fd(220)
lt(63)
fd(230)
lt(62)
fd(230)
lt(78)
fd(203)
lt(45)
fd(160)


