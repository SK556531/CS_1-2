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

x_cor = 0
Life=1

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

x1=rand.choice(x_and_y_values)
x2=rand.choice(x_and_y_values)
x3=rand.choice(x_and_y_values)
x4=rand.choice(x_and_y_values)

s.shape("turtle")
s.pensize(3)
s.pencolor("green")

picture_1='Rock_3.gif'

wn.addshape(picture_1)
t1.shape(picture_1)
l1.shape(picture_1) 
b1.shape(picture_1) 
r1.shape(picture_1) 

#-----game functions--------
def countup():
    global timer, timer_up
    global Life
    counter.clear()
    if (Life < 0):
      counter.write("GAME OVER", font=font_setup)
      timer_up = True
    else:
      counter.write("Timer: " + str(timer), font=font_setup)
      timer += 1
      counter.getscreen().ontimer(countup, counter_interval)
    if(timer!=0 and timer%12==4):
      move_rock()
    if(timer!=0 and timer%12==8) and (timer%12!=0):
      move_rock_2()    
    if (timer!=0 and timer%12==0):
      change_position_of_all()

      
      

     

 
def move_right():
  global x_cor
  x=s.xcor()+100
  y=s.ycor()
  if (x<-200 or x>200):
    x=200
    x_cor=100
  s.goto(x,y)
  x_cor == x_cor+100
 
def move_left():
  global x_cor
  x=s.xcor()-100
  y=s.ycor()
  if (x<-200 or x>200):
    x=-200
    x_cor=-100
  s.goto(x,y)
  x_cor == x_cor-100    

 
def change_position_of_t1():
    x1=rand.choice(x_and_y_values)
    t1.goto(x1,300)

def change_position_of_b1():
    x2=rand.choice(x_and_y_values)
    b1.goto(x2,300)

def change_position_of_l1():
    x3=rand.choice(x_and_y_values)
    l1.goto(x3,300)

def change_position_of_r1():
    x4=rand.choice(x_and_y_values)
    r1.goto(x4,300)

def change_position_of_all():
  '''
  t1.hideturtle()
  b1.hideturtle()
  l1.hideturtle()
  r1.hideturtle()
  '''
  change_position_of_t1()
  change_position_of_l1()
  change_position_of_b1()
  change_position_of_r1()
  t1.showturtle()
  b1.showturtle()
  l1.showturtle()
  r1.showturtle()

def move_rock():
  global Life
  global x_cor
  x_cor = s.xcor() 
  tx=t1.xcor()
  lx=l1.xcor()
  bx=b1.xcor()
  rx=r1.xcor()  
  t1.goto(tx,0)
  l1.goto(lx,0)
  b1.goto(bx,0)
  r1.goto(rx,0)
  if (tx==x_cor or lx==x_cor or bx==x_cor or rx==x_cor):
    GAME_OVER()
def move_rock_2():
  tx=t1.xcor()
  lx=l1.xcor()
  bx=b1.xcor()
  rx=r1.xcor()  
  t1.goto(tx,-300)
  l1.goto(lx,-300)
  b1.goto(bx,-300)
  r1.goto(rx,-300)

def GAME_OVER():
  global Life
  Life=0
  Life=-1

#-----events----------------
counter.hideturtle()
counter.penup()
counter.goto(200,250)

s.left(90)

change_position_of_t1()
t1.right(90)
 
change_position_of_b1()
b1.right(90)
 
change_position_of_l1()
l1.right(90) 
change_position_of_r1()
r1.right(90)
 
wn.onkeypress(move_left, "a")
wn.listen()
wn.onkeypress(move_right, "d")
wn.listen()

wn.onkeypress(GAME_OVER, "r")
wn.listen()



wn.bgcolor("sky blue")
wn.ontimer(countup, counter_interval)
wn.mainloop()

