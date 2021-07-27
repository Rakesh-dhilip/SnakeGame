import turtle
import random
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.8)
        self.set_position()
    def set_position(self):
        X=random.randint(-230,230)
        Y = random.randint(-230, 230)
        self.goto((X,Y))