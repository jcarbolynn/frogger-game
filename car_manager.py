from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

  def __init__(self):
    super().__init__()
    self.all_cars = []
    self.car_speed = STARTING_MOVE_DISTANCE

  def create_car(self):
    # because too many cars if generating a car every .1 seconds
    random_chance = random.randint(1,8)
    if random_chance == 1:
      new_car = Turtle("square")
      new_car.shapesize(stretch_wid = 1, stretch_len = 2)
      new_car.penup()
      new_car.color(random.choice(COLORS))
      x_cor = 300
      y_cor = random.randint(-250, 250)
      new_car.goto(x_cor, y_cor)
      self.all_cars.append(new_car)

  def drive(self):
    for car in self.all_cars:
      # car.setx(car.xcor() - STARTING_MOVE_DISTANCE)
      car.backward(self.car_speed)

  def level_up(self):
    self.car_speed += MOVE_INCREMENT
    
  
  # def __init__(self):
  #   super().__init__()
  #   self.color(random.choice(COLORS))
  #   self.shape("square")
  #   self.shapesize(stretch_wid = 1, stretch_len = 2)
  #   self.penup()
  #   self.x_cor = 300
  #   self.y_cor = random.randint(-260, 260)
    
  #   self.goto(self.x_cor, self.y_cor)

  # def drive(self):
  #   self.setx(self.xcor() - STARTING_MOVE_DISTANCE)
  #   # self.backward(STARTING_MOVE_DISTANCE)
