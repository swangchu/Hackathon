#by 1980
from turtle import*
shape("turtle")
speed(0)
pu()
setposition(0,-350)
pd()
pensize(20)
def create_circle(radius):
    circle(radius)
color("Red")    
create_circle(350)#outer circle

def position(xaxis, yaxis):
    setx(xaxis)
    sety(yaxis)

pu()    
position(0, -250)
pd()
pensize(10)
color("Green")
begin_fill()
color("cyan")
create_circle(250)#inner circle
end_fill()
pu()
setposition(0,0)
pensize(5)

for i in range(6):#drawing the lines dividing the GNH wheel
    pu()
    fd(90)
    pd()
    color("Green")
    fd(255)
    pu()
    bk(350)
    left(60)

for i in range(6):#drawing the scale
    color("Yellow")
    lt(30)
    pu()
    fd(90)
    pd()
    pensize(15)
    fd(150)
    bk(240)
    lt (30)
setposition(0,0)
pensize (94)
dot ()
color ("Orange")
pensize (70)
dot ()
color ("cyan")

pu()# writing GNH Progress Wheel at the centre
lt(225)
fd(50)

color("Black")
write("GNH\nProgress\nWheel", font=("verdana",15,"normal"))

rt(195)
setposition(0,0)
def draw_division():
    fd(94)
    write(1, font=("verdana",15,"normal"))
    fd(40)
    write(2, font=("verdana",15,"normal"))
    fd(40)
    write(3, font=("verdana",15,"normal"))
    fd(40)
    write(4, font=("verdana",15,"normal"))
    bk(214)
    lt(60)

for i in range(6):
    draw_division()

#labeling the wheel
left(60)
fd(300)
lt(100)
fd(100)
write("Leadership and Management", font=("ariel",10,"normal"))

setpos(0,0)
rt(30)
fd(310)

write("School\nCommunity\nVitality", font=("ariel",10,"normal"))

setpos(0,0)
lt (60)
fd (325)
write("Holistic\nAssessment", font=("ariel",10,"normal"))

setpos (0,0)
lt(45)
fd (325)
write("Broader\nLearning", font=("ariel",10,"normal"))

setpos (0,0)
lt(65)
fd (280)
write("Curriculum\nPractice", font=("ariel",10,"normal"))

setpos (0,0)
lt(60)
fd (270)
write("Green\nSchool", font=("ariel",10,"normal"))

setpos(0,0)# draw target 
pensize(2)
lt(60)
pu()
fd(180)
pd()
num1 = input("Enter the color of Current Rating: ")
color(num1)

rt(120)
fd(180)
rt(60)
fd(180)

rt(65)
fd(170)
rt(70)
fd(150)

rt(30)
fd(150)
rt(75)
fd(174)

num2 = input("Enter the color of Target: ")# draw current rating
color(num2)

lt(55)
pu()
fd(40)
pd()

rt(115)
fd(200)
rt(60)
fd(225)

rt(73)
fd(190)

rt(50)
fd(175)

rt(46)
fd(180)

rt(70)
fd(220)

color(num1)
rt(30)
pu ()
fd (400)
pd ()
shape ("square")
pensize (40)
stamp ()
pu ()
fd (30)
pd ()
write("Target", font=("Bernard",10,"normal"))

color(num2)
rt (90)
pu ()
fd (50)
pd ()
stamp ()
write("        Current Rating", font=("Bernard",10,"normal"))
ht()












