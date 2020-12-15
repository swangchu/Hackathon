from turtle import*
shape("turtle")
speed(0)

lt(90)
pensize(15)
color("indigo")
for i in range(6):
    pu()
    fd(80)
    pd()
    fd(180)
    bk(180)
    pu()
    bk(80)
    lt(60)

rt(90)
color("silver")
pensize(5)
for i in range(6):
    pu()
    fd(80)
    pd()
    fd(260)
    bk(260)
    pu()
    bk(80)
    lt(60)
#center circle
pu()
goto(0, -80)
begin_fill()
color("yellow")
circle(80)
end_fill()

pu()
goto(0, -60)
begin_fill()
color("grey")
circle(60)
end_fill()

def draw_circle(rad,col):
    color(col)
    circle(rad)
#outer circle
pu()
goto(340,0)
pd()
lt(90)
pensize(10)
draw_circle(340,"maroon")

#inner circle
pu()
goto(0, 265)  
pd()
lt(90)
pensize(10)
draw_circle(265,"green")


pu()
goto(-15,28)
pd()
color("black")

pu()
goto(3,-29)
pd()
write("   GNH \n Pogress \n  Wheel", align="center", font=("Verdana", 15, "normal"))
pu()
goto(0,-310)
pd()
write("Broader Learning", align="center", font=("Verdana", 10, "normal"))
pu()
goto(260,-160)
pd()
write("   Curriculum\n  Practice", align="center", font=("Verdana", 10, "normal"))

pu()
goto(0, 283)
pd()

write("Leadership and Management", align="center", font=("Verdana", 10, "normal"))
pu()
goto(-230,160)
pd()
write("School\nCommu-\nnity-\nVitality", align="center", font=("Verdana", 10, "normal"))
pu()
goto(250,150)
pd()
write("Green \n School", align="center", font=("Verdana", 10, "normal"))
pu()
goto(-260,-160)
pd()
write("Holistic\nAssessment", align="center", font=("Verdana", 10, "normal"))
pu()
goto(0,80)
pd()
rt(180)
color("white")
write(" 4\n\n 3 \n\n 2 \n\n 1", align="center", font=("Verdana", 15, "normal"))
pu()
goto(0,-260)
pd()
write(" 1\n\n 2 \n\n 3 \n\n 4", align="center", font=("Verdana", 15, "normal"))

pu()
goto(70,40)
pd()
write("\t\t\t4\n\t\t        3\n\t\t  2\n\t          1", align="center", font=("Verdana", 15, "normal"))

pu()
goto(-240,-136)
pd()
write("\t\t\t 1 \n\t\t          2 \n\t \t    3\t \n\t             4", align="center", font=("Verdana", 15, "normal"))

pu()
goto(-70,40)
pd()
write("4\t\t\t\n      3 \t\t\n            2     \t\n                   1     ", align="center", font=("Verdana", 15, "normal"))

pu()
goto(250,-135)
pd()
write("1\t\t\t    \n      2 \n            3 \n\t    4", align="center", font=("Verdana", 15, "normal"))

pencolor("black")
pensize(3)
penup()
setposition(0,-200)
pd()

setposition(220,-130)

setposition(220,130)

setposition(0,240)

setposition(-220,130)

setposition(-213,-130)

setposition(0,-200)


rate1 = int(input("rate for Broader Learning: "))
rate2 = int(input("rate for Curriculum Practice: "))
rate3 = int(input("rate for Green School: "))
rate4 = int(input("rate for Leadership and Management: "))
rate5 = int(input("rate for School community-Vitality: "))
rate6 = int(input("rate for Holistic Assessment: "))

pu()
goto(0,0)
pd()
if rate1 < 5 :
    goto(0, -198)
elif rate2 < 5 :
    goto(198, -125)
elif rate3 < 5 :
    goto(198, 125)
    






















