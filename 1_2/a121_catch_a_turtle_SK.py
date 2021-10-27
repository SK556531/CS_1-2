# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl4
import turtle as trtl
import random as rand
import turtle as trtl2
import turtle as trtl3

#-----game configuration----
spot = trtl.Turtle()
score_writer = trtl2.Turtle()
counter = trtl3.Turtle()
start_button = trtl4.Turtle()
spot_shape="circle"
spot_color="green"
spot_fillcolor="green"
spot_size=2
spot_speed=0
score=0
score_writer_color="green"
counter_color="red"
start_font=("Arial",100,"normal")
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----new spot variable-------
list_color = ["red","blue","green","yellow","white","black"]
list_size = [1,2,3,5]

#-----initialize turtle-----
spot.shape(spot_shape)
spot.color(spot_color)
spot.fillcolor(spot_fillcolor)
spot.shapesize(spot_size)
spot.speed(spot_speed)
score_writer.color(score_writer_color)
counter.color(counter_color)
start_button.shape(spot_shape)
start_button.shapesize(10)
#-----game functions--------
def spot_clicked(x,y):
  if (timer_up!=True):
    update_score()
    make_new_spot()
    change_position()
  
  else:
    spot.hideturtle()

def make_new_spot():
  spot.stamp()
  new_color = rand.choice(list_color)
  new_size = rand.choice(list_size)
  spot.color(new_color)
  spot.shapesize(new_size)
  

def change_position():
  new_xpos=rand.randint(-400,400)
  new_ypos=rand.randint(-300,300)
  spot.penup()
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.pendown()
  spot.showturtle()
def update_score():
  global score
  score+=1
  if (score != 1):
    score_writer.clear()
  score_writer.write(score, font=font_setup)
def draw_box():
  spot.pendown()
  for t in range(2):
    spot.forward(125)
    spot.lt(90)
    spot.forward(45)
    spot.lt(90)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def start_game(x,y):
  timer=31
  start_button.penup()
  start_button.hideturtle()
  start_button.goto(-100,100)
  start_button.write("Start",start_font)
  start_button.goto(-400,-400)
  start_button.clear()
  spot.showturtle()
#-----events----------------
spot.hideturtle()
spot.penup()
spot.goto(320,350)
draw_box()
spot.penup()
spot.goto(175,350)
draw_box()
spot.penup()
spot.goto(0,0)


score_writer.penup()
score_writer.goto(330,350)

counter.penup()
counter.goto(180,350)
start_button.goto(0,0)



start_button.onclick(start_game)
spot.onclick(spot_clicked)



wn = trtl.Screen()
wn.bgcolor("sky blue")
wn.ontimer(countdown, counter_interval)
wn.mainloop()