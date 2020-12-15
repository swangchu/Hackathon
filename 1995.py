from turtle import*
#This program represents GNH Progress Wheel
speed(0)
def draw_hash(): 
    fd(30)
    rt(90)
    fd(10)
    fd(-20)
    fd(10)
    lt(90)
def number_1(): 
    right(90)
    penup()
    fd(20)
    left(180)
    pendown()
    write("1")
    penup()
    fd(20)
    pendown()
    right(90)

def number_2():
    right(90)
    penup()
    fd(20)
    left(180)
    pendown()
    write("2")
    penup()
    fd(20)
    pendown()
    right(90)

def number_3():
    right(90)
    penup()
    fd(20)
    left(180)
    pendown()
    write("3")
    penup()
    fd(20)
    pendown()
    right(90)

def number_4():
    right(90)
    penup()
    fd(20)
    left(180)
    pendown()
    write("4")
    penup()
    fd(20)
    pendown()
    right(90)


penup()
sety(-40)
pendown()
for i in range(6): # drawing 6 lines with 6 squares
    right(90)
    color("lightgreen")
    draw_hash()
    number_1()
    draw_hash()
    number_2()
    draw_hash()
    number_3()
    draw_hash()
    number_4()
    fd(30)
    right(90)
    begin_fill()
    color("lightblue")
    circle(60, 360, 4)
    end_fill()
    right(90)
    fd(150)
    penup()
    right(90)
    circle(60, 60, 10)
    pendown()

begin_fill()    #Drawing a circle
color("green")
pensize(10)
circle(60)
end_fill()

penup()     #Wordings inside the circle
setposition(-85,20)
fd(70)
pendown()
color("black")
write("GNH", font=("Verdana", 10, "normal"))
penup()
right(90)
fd(20)
left(90)
fd(-35)
pendown()
write("Progress Wheel", font=("Verdana", 10, "normal"))

penup()    #Holistic Assessment
setposition(-260,-100)
pendown()
write("Holistic ", font=("Verdana", 10, "normal"))
pendown()
penup()
right(90)
fd(20)
left(90)
fd(-10)
pendown()
write("Assessment", font=("Verdana", 10, "normal"))

penup()      #School Community Vitality
sety(170)
fd(5)
pendown()
write("School ", font=("Verdana", 10, "normal"))
pendown()
penup()
right(90)
fd(20)
left(90)
pendown()
write("Community ", font=("Verdana", 10, "normal"))
penup()
right(90)
fd(20)
left(90)
pendown()
write("Vitality ", font=("Verdana", 10, "normal"))

penup()    #Green School
setx(210)
left(90)
fd(30)
right(90)
pendown()
write("Green ", font=("Verdana", 10, "normal"))
pendown()
penup()
right(90)
fd(20)
left(90)
pendown()
write("School ", font=("Verdana", 10, "normal"))

penup()    #Curriculum Practice
sety(-115)
fd(-15)
pendown()
write("Curriculum ", font=("Verdana", 10, "normal"))
pendown()
penup()
right(90)
fd(20)
left(90)
fd(5)
pendown()
write("Practice ", font=("Verdana", 10, "normal"))

penup()    #Broader Learning
setposition(-30,-250)
pendown()
write("Broader ", font=("Verdana", 10, "normal"))
pendown()
penup()
right(90)
fd(20)
left(90)
pendown()
write("Learning ", font=("Verdana", 10, "normal"))

penup()    #Leadership And Management
sety(295)
fd(-7)
pendown()
write("Leadership & ", font=("Verdana", 10, "normal"))
pendown()
penup()
right(90)
fd(15)
left(90)
#fd(5)
pendown()
write("Management", font=("Verdana", 10, "normal"))


penup()                      #Target Ratings and Current Ratings
setposition(0,20)
right(90)
fd(160)
left(90)
begin_fill()
color("red")
circle(10,360,3)
end_fill()
left(90)
fd(15)
right(90)
begin_fill()
color("black")
circle(10)
end_fill()
right(90)
fd(15)
left(90)

left(90)
penup()
fd(330)
right(90)
begin_fill()
color("red")
circle(10,360,3)
end_fill()
right(90)
fd(30)
left(90)
begin_fill()
color("black")
circle(10)
end_fill()
right(90)
fd(-20)
left(90)


penup()
setposition(0,20)
left(30)
fd(170)
right(90)
begin_fill()
color("red")
circle(10,360,3)
end_fill()
right(90)
fd(20)
left(90)
begin_fill()
color("black")
circle(10)
end_fill()
left(90)
fd(20)
right(90)
pendown()



penup()
setx(-150)
left(110)
begin_fill()
color("red")
circle(10,360,3)
end_fill()
rt(90)
fd(30)
lt(90)
begin_fill()
color("black")
circle(10)
end_fill()
rt(90)
fd(-30)
lt(90)
pendown()


penup()
sety(-90)
fd(35)
begin_fill()
color("red")
circle(10,360,3)
end_fill()
rt(20)
fd(33)
begin_fill()
color("black")
circle(10)
end_fill()
rt(-20)
fd(-33)
pendown()


penup()
setx(160)
right(175)
rt(90)
fd(4)
lt(90)
right(-90)
fd(-10)
right(90)
begin_fill()
color("red")
circle(10,360,3)
end_fill()
right(90)
fd(10)
right(90)
begin_fill()
color("black")
circle(10)
end_fill()
pendown()

penup()                    #Keywords
setposition(280,240)
pendown()
begin_fill()
color("red")
circle(10, 360, 3)
end_fill()
penup()
rt(45)
fd(10)
write("Target Rating")
penup()
fd(20)
pendown()

penup()
setposition(280,205)
pendown()
begin_fill()
color("black")
circle(10)
end_fill()
penup()
fd(15)
pendown()
write("Current Rating")

