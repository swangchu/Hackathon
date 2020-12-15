from turtle import *
shape ("turtle")
speed(0)
#Outer Circle Divider
pu()
goto(0,0)
pd()
for i in range(6):
    pensize(5)
    color("gold")
    fd(300)
    bk(300)
    lt(60)
#Inner Circle Divider   
pu()
goto(0,0)
pd()
rt(30)
for i in range(6):
    pensize(15)
    color("silver")
    rt(60)
    fd(250)
    bk(250)

#The following code is for drawing the inner two circles(forestgreen & brown)
lt(30)
goto(0, -100)
def draw_circle(radius,col):
    begin_fill()
    color("royal blue")
    circle(radius)
    color(col)
    end_fill()
draw_circle(int("100"), "royal blue")
lt(90)
pu()
fd(25)
rt(90)
draw_circle(int("75"), "linen")


#The following code is to draw the outer circles (orange & grey)
def draw_circle1(radius, col1):
    pensize(15) 
    circle(radius)
    color(col1)

color("gold")
rt(90)
pu()
fd(175)
lt(90)
pd()
draw_circle1 (int("250"), "gold")

color("silver")
rt(90)
pu()
fd(50)
lt(90)
pd()
draw_circle1 (int("300"), "silver")

#The following code is to write the main text
penup()
goto(-135,-30)
pendown()
write(''' \tGNH
             Progress
               wheel''', font=("verdana",15, "bold"))

pu()
setposition(0,0)
pd()

color("black")

def angle1():
       angle= float(input("Please enter the angle:"))
       rt(angle)
       penup()
       forward(130)
       pd()
    
def numbering_integers():
        write("1", font=("Verdana",12, "bold"))
        pu()
        fd(30)
        pd()
        write("2", font=("Verdana",12, "bold"))
        pu()
        fd(30)
        pd()
        write("3", font=("Verdana",12, "bold"))
        pu()
        fd(30)
        pd()
        write("4", font=("Verdana",12, "bold"))
        pu()
        bk(250)
        setposition(0,0)
        pd()
        
for i in range(6):
    angle1()
    numbering_integers()


#THE FOLLOWING CODE IS THE NAME FOR EACH PIE
pu()

fd(250)
write("green school", font = ("verdana",10,"bold"))

goto(0,-280)
write("Broader Learning", font = ("verdana",10,"bold"))

goto(200 , -200)
write("curriculum practice", font = ("verdana",10,"bold"))

goto(-200 , -200)
write(" holistic assessment", font = ("verdana",10,"bold"))

goto(-200 , 150)
write(" school community-vitality ", font = ("verdana",10,"bold"))

goto(0 , 280)
write("  leadership and management ", font = ("verdana",10,"bold"))




