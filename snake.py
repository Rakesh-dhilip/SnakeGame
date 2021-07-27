from turtle import Turtle,Screen
import time
screen=Screen()
position=[(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for i in position:
            new_body=Turtle()
            new_body.penup()
            new_body.shape("square")
            new_body.color("white")
            new_body.goto(i)
            self.segments.append(new_body)




    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[i - 1].pos()
            self.segments[i].goto(pos)
        self.segments[0].forward(20)

    def up(self):
        if(self.head.heading()!=270):
            self.segments[0].setheading(90)

    def down(self):
        if (self.head.heading()!= 90):

            self.segments[0].setheading(270)

    def right(self):
        if (self.head.heading()!= 180):

            self.segments[0].setheading(360)

    def left(self):
        if(self.head.heading()!=0):

            self.segments[0].setheading(180)

    def eat(self):

        new_body = Turtle()
        new_body.penup()
        new_body.shape("square")
        new_body.color("white")
        new_body.goto(self.segments[-1].position())
        self.segments.append(new_body)
