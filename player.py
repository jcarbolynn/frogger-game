from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):

  def __init__(self):
    super().__init__()
    self.color("black")
    self.shape("turtle")
    self.penup()
    self.go_to_start()
    # originally had the below instead of using the method, later when made go_to_start, replaced because it was repetetive
    # self.goto(STARTING_POSITION)
    self.setheading(UP)

  def up(self):
    self.forward(MOVE_DISTANCE)
    # self.sety(self.ycor() + MOVE_DISTANCE)

  def is_at_finish(self):
    if self.ycor() > FINISH_LINE_Y:
      return True
    else:
      return False

  def go_to_start(self):
    self.goto(STARTING_POSITION)
    
