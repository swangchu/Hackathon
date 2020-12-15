from turtle import *
shape('arrow')
speed(0)
bgcolor("aqua")
color("plum")
begin_fill()
pu()

#small circle
goto(0,-50)
pd()
circle(50)
end_fill()

#small second circle
color("red")
begin_fill()
pu()    
goto(0,-60)
pd()
circle(60)
end_fill()

pu()
goto(0,0)
#second outer most circle
color("green")
goto(0,-200)
pd()
width(10)
circle(200)
#outer most circle
pencolor("maroon")
pu()
goto(0,-290)
pd()
circle(300)


pu()
goto(0,0)
pd()

for i in range(6):
   pencolor('firebrick')
   width(5)
   pu()
   fd(62)
   pd()
   fd(240)
   pu()
   goto(0,0)
   bk(62)
   pd()
   bk(240)
   pu()
   goto(0,0)
   lt(60)
   pu()
   fd(62)
   pd()
   fd(240)
   pu()
   goto(0,0)

rt(90)
for i in range(6):
   pencolor('forestgreen')
   width(15)
   pu()
   fd(62)
   pd()
   fd(140)
   pu()
   goto(0,0)
   bk(62)
   pd()
   bk(140)
   pu()
   goto(0,0)
   lt(60)
   pu()
   fd(140)
   pd()
   pu()
   goto(0,0)


  
# import package
from turtle import*
goto(-100,250)
lt(90)
# write text
color("black")
write("Leadership and Management")

goto(-100,-250)
write("Broader Learning")

goto(130,-200)
lt(170)
write("Curriculum Practice")

goto(180,160)
lt(90)
write("Green School")


goto(-270,90)
lt(180)
write("School Community - Vitality")


goto(-220,-170)
lt(180)
write("Holistic Assessment")

goto(-4,20)
write("GNH")
goto(-20,0)
write("Progress")
goto(-4,-20)
write("Wheel")


lt(10)
goto(0,0)
pu()
fd(70)
pd()
dot(10,"black")
pu()
fd(40)
dot(10,"brown")

pu()
fd(40)
dot(10,"red")

pu()
fd(40)
dot(10,"yellow")




pu()
goto(0,0)
rt(60)
pu()
fd(70)
pd()
dot(10,"black")
pu()
fd(40)
dot(10,"brown")

pu()
fd(40)
dot(10,"red")

pu()
fd(40)
dot(10,"yellow")


pu()
goto(0,0)
rt(180)
pu()
fd(70)
pd()
dot(10,"black")
pu()
fd(40)
dot(10,"brown")

pu()
fd(40)
dot(10,"red")

pu()
fd(40)
dot(10,"yellow")



pu()
goto(0,0)
rt(60)
pu()
fd(70)
pd()
dot(10,"black")
pu()
fd(40)
dot(10,"brown")

pu()
fd(40)
dot(10,"red")

pu()
fd(40)
dot(10,"yellow")



pu()
goto(0,0)
rt(180)
pu()
fd(70)
pd()
dot(10,"black")
pu()
fd(40)
dot(10,"brown")

pu()
fd(40)
dot(10,"red")

pu()
fd(40)
dot(10,"yellow")




pu()
goto(0,0)
rt(60)
pu()
fd(70)
pd()
dot(10,"black")
pu()
fd(40)
dot(10,"brown")

pu()
fd(40)
dot(10,"red")

pu()
fd(40)
dot(10,"yellow")


pencolor("grey")
width(5)
lt(120)
pd()
fd(200)

lt(75)
pd()
fd(180)
   
    
 
 
lt(47)
pd()
fd(150)
   
lt(48)
pd()
fd(165)

lt(68)
pd()
fd(186)

lt(60)
pd()
fd(185)
pu()
#representation of target
goto(400,300)
pd()
dot(20,"grey")
pu()
fd(20)
write("Target")

#Ratings
goto(400,200)
dot(20,"black")
pu()
fd(20)
write("ONE")





goto(400,150)
dot(20,"brown")
pu()
fd(20)
write("TWO")



goto(400,100)
dot(20,"red")
pu()
fd(20)
write("THREE")
     

     
goto(400,50)
dot(20,"yellow")
pu()
fd(20)
write("FOUR")
#current Rating
pu()
goto(-500,200)

write("Leadership and Management 3")
write("school community - vitality  3")
write("Holistic Assessment 2")
write("Broader Learning 3")
write("curriculum Practice 3")
write("Green School 3")







    
