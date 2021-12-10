# SK_Project_1.3.1
#-----import statements-----
 
 
#-----game configuration----
import turtle as trtl
import turtle as trtl2
import turtle as trtl3
import turtle as trtl4
import turtle as trtl5
import turtle as trtl6
import random as rand

x_and_y_values = [-200,-100,0,100,200]
 
#-----countup variables-----
font_setup = ("Arial", 20, "normal")
timer = 0
counter_interval = 1000   #1000 represents 1 second
timer_up = False

 
#-----initialize turtle-----
s = trtl.Turtle()
wn = trtl.Screen()
s.penup()
t1=trtl2.Turtle()
l1=trtl3.Turtle()
b1=trtl4.Turtle()
r1=trtl5.Turtle()
counter=trtl6.Turtle()
 
t1.penup()
l1.penup()
b1.penup()
r1.penup()
'''
picture_1='LB1110.gif'

wn.addshape(picture_1)
t1.shape(picture_1)
l1.shape(picture_1) 
b1.shape(picture_1) 
r1.shape(picture_1) 
''''
#-----game functions--------
def countup():
    global timer, timer_up
    counter.clear()
    if timer < 0:
      counter.write("GAME OVER", font=font_setup)
      timer_up = True
    else:
      counter.write("Timer: " + str(timer), font=font_setup)
      timer += 1
      counter.getscreen().ontimer(countup, counter_interval)
      move_rock()
      change_position_when_dissapered()
      
      if ():
          change_position_of_all()
        
     
def move_rock():
    if (t1.ycor == -300):
      change_position_of_all()
    t1.forward(50)
    l1.forward(50)
    b1.forward(50)
    r1.forward(50)
    if (t1.xcor == s.xcor and t1.ycor == s.ycor):
        timer=-1
    if (l1.xcor == s.xcor and l1.ycor == s.ycor):
        timer=-1
    if (b1.xcor == s.xcor and b1.ycor == s.ycor):
        timer=-1
    if (r1.xcor == s.xcor and r1.ycor == s.ycor):
        timer=-1
 
def move_right():
    x=s.xcor()+100
    y=s.ycor()
    if (x<-200 or x>200):
        x=200
    s.goto(x,y)
 
def move_left():
    x=s.xcor()-100
    y=s.ycor()
    if (x<-200 or x>200):
        x=-200
    s.goto(x,y)
 
def move_up():
    x=s.xcor()
    y=s.ycor()+100
    if (y<-200 or y>200):
        y=200
    s.goto(x,y)
 
def move_down():
    x=s.xcor()
    y=s.ycor()-100
    if (y<-200 or y>200):
        y=-200
    s.goto(x,y)
 
def change_position_of_t1():
    x1=rand.choice(x_and_y_values)
    t1.goto(x1,300)

def change_position_of_b1():
    x2=rand.choice(x_and_y_values)
    b1.goto(x2,-300)

def change_position_of_l1():
    y1=rand.choice(x_and_y_values)
    l1.goto(-300,y1)

def change_position_of_r1():
    y2=rand.choice(x_and_y_values)
    r1.goto(300,y2)

def change_position_of_all():
  change_position_of_t1()
  change_position_of_l1()
  change_position_of_b1()
  change_position_of_r1()

def change_position_when_dissapered():
  if(t1.ycor<-300):
    change_position_of_all()
#-----events----------------
counter.hideturtle()
counter.penup()
counter.goto(200,250)
 
change_position_of_t1()
t1.right(90)
 
change_position_of_b1()
b1.left(90)
 
change_position_of_l1()
 
change_position_of_r1()
r1.right(180)
 
wn.onkeypress(move_left, "a")
wn.listen()
wn.onkeypress(move_right, "d")
wn.listen()
wn.onkeypress(move_up, "w")
wn.listen()
wn.onkeypress(move_down, "s")
wn.listen()
wn.onkeypress(change_position_of_all, "r")
wn.listen()



wn.bgcolor("sky blue")
wn.ontimer(countup, counter_interval)
wn.mainloop()

