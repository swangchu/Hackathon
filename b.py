from turtle import*
shape("turtle")
speed(0)
penup()
bgcolor("green")


################## Drawing the SSA
setposition(0,-350)
pendown()
pensize(4)
circle(350)
penup()
setposition(0,0)
pendown()
color("yellow")
for i in range(6):  #division of the circle
    left(60)
    forward(350)
    backward(350)
penup()
setposition(0,0) 
pensize(10)
color("black")
left(30)
pendown()
for i in range(6):
    fd(350)
    backward(350)
    left(60)
penup()
setposition(-70,310) #position of turtle to indicator 1
pendown()
color("cyan")
write("(Leadership and Management")                       
penup()
setposition(-310,160) #position of turtle to indicator 2
write("(School Community - Vitality)")
penup()
setposition(-305,-190)#position of turtle to indicator 3
write("(Holistic Assessment)")
setposition(-50,-310)  #position of turtle to indicator 4
write("(Broader learning)")
setposition(200,-190) #position of turtle to indicator 5
write("(Curciculum Practice)")
setposition(200,160)#position of turtle to indicator 6
write("(Green School)")
setposition(0,0)



def score1():
    score = 1
    for i in range(4):
        forward(60)
        write(score, font = ("Calibri",15, "normal"))
        score = score + 1
    backward(240)
for i in range(6):
    score1()
    left(60)
################ ASking for Input

max_rating = 5
crating1 = 0
crating2 = 0
crating3 = 0
crating4 = 0
crating5 = 0
crating6 = 0


targetrating1 = 0

targetrating2 = 0
targetrating3 = 0
targetrating4 = 0
targetrating5 = 0
targetrating6 = 0

crating_1 = float(input("1)i) Enter current rating for Leadership and management: ")) #current rating for indicator 1
crating1 = crating_1
if crating1 >= max_rating:
            print("invalid rating (rating cannot exceed 4)")
            crating_1 = float(input("1.Enter current rating for Leadership and management: "))

targetrating_1 = float(input("1)ii)Enter target rating for Leadership and management: ")) #target rating for indicator 1
targetrating1 = targetrating_1
if targetrating1 >= max_rating:
    print("invalid rating (rating cannot exceed 4)")
    targetrating1 = float(input("Enter target rating for Leadership and management: "))


##################
crating_2 = float(input("2)i).Enter current rating for School Community - Vitality: ")) #current rating for indicator 2
crating2 = crating_2
if crating2 >= max_rating:
            print("invalid rating (rating cannot exceed 4)")
            crating_2 = float(input(".Enter current rating for School Community - Vitality: "))

targetrating_2 = float(input("2)ii)Enter target rating for School Community - Vitality: ")) #target rating for indicator 2
targetrating2 = targetrating_2
if targetrating1 >= max_rating:
    print("invalid rating (rating cannot exceed 4)")
    targetrating1 = float(input("Enter target rating for School Community - Vitality: "))

###################
crating_3 = float(input("3)i).Enter current rating for Holistic Assessment: ")) #current rating for indicator 3
crating3 = crating_3
if crating3 >= max_rating:
            print("invalid rating (rating cannot exceed 4)")
            crating_3 = float(input("Enter current rating for Holistic Assessment: "))


targetrating_3 = float(input("3)ii)Enter target rating for Holistic Assessment: ")) #target rating for indicator 3
targetrating3 = targetrating_3
if targetrating3 >= max_rating:
    print("invalid rating (rating cannot exceed 4)")
    targetrating3 = float(input("Enter target rating for Holistic Assessment: "))


####################
crating_4 = float(input("4)i).Enter current rating for Broader Learning: ")) #current rating for indicator 4
crating4 = crating_4
if crating1 >= max_rating:
            print("invalid rating (rating cannot exceed 4)")
            crating_4 = float(input("1.Enter current rating for Broader Learning: "))

   


targetrating_4 = float(input("4)ii)Enter target rating for Broader Learning: ")) #target rating for indicator 4
targetrating4 = targetrating_4
if targetrating4 >= max_rating:
    print("invalid rating (rating cannot exceed 4)")
    targetrating4 = float(input("Enter target rating for Broader Learning: "))


#####################
crating_5 = float(input("5)i).Enter current rating for Curriculum Practice: ")) #current rating for indicator 5
crating5 = crating_5
if crating5 >= max_rating:
            print("invalid rating (rating cannot exceed 4)")
            crating_5 = float(input("1.Enter current rating for Curriculum Practice: "))


targetrating_5 = float(input("5)ii)Enter target rating for Curriculum Practicet: ")) #target rating for indicator 5
targetrating5 = targetrating_5
if targetrating5 >= max_rating:
    print("invalid rating (rating cannot exceed 4)")
    targetrating5 = float(input("Enter target rating for Curriculum Practice: "))

##########################
crating_6 = float(input("6)i).Enter current rating for Green School: ")) #current rating for indicator 6
crating6 = crating_6
if crating1 >= max_rating:
            print("invalid rating (rating cannot exceed 4)")
            crating_6 = float(input("1.Enter current rating for Leadership and management: "))


targetrating_6 = float(input("6)ii)Enter target rating for Green School: ")) #target rating for indicator 6
targetrating6 = targetrating_6
if targetrating6 >= max_rating:
    print("invalid rating (rating cannot exceed 4)")
    targetrating6 = float(input("Enter target rating for Green School: ")) 
  

#####################
    
penup()
pensize(2)

if crating1 == 1:  # Positioning of rebap to the score
    setposition(0,70)
elif crating1 == 2:
    setposition(0,120)
elif crating1 == 3:
    setposition(0,190)
else:
    setposition(0,240)

pendown()
if crating2 == 1:  # Positioning of rebap to the score
    setposition(-50,30)
elif crating2 == 2:
    setposition(-100,60)
elif crating2 == 3:
    setposition(-150,80)
else:
    setposition(-200,120)



 
if crating3 == 1:  # Positioning of rebap to the score
    setposition(-50,-30)
elif crating3 == 2:
    setposition(-100,-60)
elif crating3 == 3:
    setposition(-150,-80)
else:
    setposition(-200,-110)

 


if crating4 == 1:  # Positioning of rebap to the score
    setposition(0,-70)
elif crating4 == 2:
    setposition(0,-120)
elif crating4 == 3:
    setposition(0,-170)
else:
     setposition(0,-220)




if crating5 == 1:  # Positioning of rebap to the score
    setposition(50,-30)
elif crating5 == 2:
    setposition(100,-60)
elif crating5 == 3:
    setposition(150,-90)
else:
    setposition(200,-120)





if crating6 == 1:  # Positioning of rebap to the score
    setposition(50,30)
    setposition(0,70)
elif crating6 == 2:
    setposition(100,60)
    setposition(0,120)
elif crating6 == 3:
    setposition(150,90)
    setposition(0,190)
else:
    setposition(200,120)
    setposition(0,240)
##########
penup()
right(30)
forward(400)
pendown()
begin_fill()
for i in range(4):
    fd(20)
    left(90)
end_fill()
penup()
fd(40)
write("Current Rating")
    





