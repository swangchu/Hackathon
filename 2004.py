
#This will wish the users according to time
import datetime
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        print('good morning, this program is used for making graphical presentation on the curretn rating of our school ')
    elif hour >= 12 and hour <18:
        print('good afternoon,this program is used for making graphical presentation on the curretn rating of our school')
    else:
        print('good evening,this program is used for making graphical presentation on the curretn rating of our school')
wish_user()
print('purple color: target rating')
print('orange color: current rating')
from turtle import*
shape('turtle')

#this program is used for making graphical presentation on the curretn rating of our school
speed(0)
bgcolor("ivory")
#the significance of this color is that it represnts light.

#inner circle
def inner_circle(radius,color_choice):
    pu()
    setposition(0,-60)
    pendown()
    pensize(6)
    color(color_choice)
    circle(radius)
    penup()
inner_circle(60,'greenyellow')
    
setposition(0,-15)
pendown()
color('red')
write('GNH',font=('Verdana',20,'normal'),align='center')



#drawing the first circle
penup()

setposition(0,-60)
pendown()

rt(90)
color('greenyellow')
fd(150)
penup()
fd(90)
lt(90)
pendown()
color('green')
#Significance of color green is that it is eco-friendly and symbolizes peace
circle(45)
lt(90)
penup()
fd(30)

write('green school', font=('Verdana',10,'normal'),align='center')

penup()
fd(60)
number = 0


for i in range(4):
 penup()
 fd(30)
 pendown()
 color('black')
 number = number + 1
 write(number, font=('Verdana',10,'normal'),align='right')
penup()







#drawing the second circle
setposition(0,60)

pendown()
color("greenyellow")
fd(150)
penup()
fd(90)
lt(90)
pendown()
color('rosybrown')
circle(45)
lt(90)
penup()
fd(50)


write('leadership', font=('Verdana',10,'normal'),align='center')
penup()
fd(60)
number = 0
for i in range(4):
 penup()
 fd(30)
 pendown()
 color('black')
 number = number + 1
 write(number, font=('Verdana',10,'normal'),align='right')
penup()


#drawing the third circle
home()

setposition(-40,40)
lt(135)
pendown()


color('greenyellow')
fd(150)
penup()
fd(90)
lt(90)
pendown()
color('black')

#black represnts boldness and it symbolises strength as our school community should be strong and united.
circle(45)
lt(90)
penup()
fd(50)

write('schoolcommunity', font=('Verdana',6,'normal'),align='center')
penup()
fd(60)
number = 0
for i in range(4):
 penup()
 fd(30)
 pendown()
 color('black')
 number = number + 1
 write(number, font=('Verdana',10,'normal'),align='right')
penup()



#drawing the fourth circle
home()
setposition(40,40)
lt(45)
pendown()

color("greenyellow")
fd(150)
penup()
fd(90)
lt(90)
pendown()
color('cyan')
circle(45)
lt(90)
penup()
fd(40)


write('curriculum practice', font=('Verdana',6,'normal'),align='center')
penup()
fd(60)

number = 0
for i in range(4):
 penup()
 fd(30)
 pendown()
 color('black')
 number = number + 1
 write(number, font=('Verdana',10,'normal'),align='right')
penup()

#drawing the fifth circle
home()
setposition(40,-40)
rt(45)
pendown()

color("greenyellow")
fd(150)
penup()
fd(90)
lt(90)
pendown()
color('crimson')
circle(45)
lt(90)
penup()
fd(40)


write('holistic assesment', font=('Verdana',6,'normal'),align='center')
penup()
fd(60)
number = 0
for i in range(4):
 penup()
 fd(30)
 pendown()
 color('black')
 number = number + 1
 write(number, font=('Verdana',10,'normal'),align='right')
penup()



#drawing the sixth circle
home()
setposition(-40,-40)
rt(135)
pendown()

color("greenyellow")
fd(150)
penup()
fd(90)
lt(90)
pendown()
color('blue')
#the color blue represents trust and faith.
circle(45)
lt(90)
penup()
fd(40)


write('broader learning', font=('Verdana',6,'normal'),align='center')



#this is for making the rating number 
penup()
fd(60)
def number1():
 number = 0
 for i in range(4):
     penup()
     fd(30)
     pendown()
     color('black')
     number = number + 1
     write(number, font=('Verdana',10,'normal'),align='center')

number1()


# this is the code which will show the rating which is provided by the user.
pensize(3)
penup()
home()
rt(90)
fd(75)
lt(90)
pendown()
color('purple')
circle(75)
#this is the code which will show the current rating.
rt(90)
penup()
fd(35)
pendown()
lt(90)
color('orange')
circle(100)
penup()
fd(200)
pendown()
color('purple')

dot(20)
write('target rating', font=('Verdana',10,'normal'),align='right')
penup()
fd(200)
pendown()
color('orange')
dot(20)

write('current rating', font=('Verdana',10,'normal'),align='right')
fd(20)






