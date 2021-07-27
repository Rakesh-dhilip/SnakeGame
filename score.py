from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.point=0
        self.color("white")
        self.goto((0,270))
        self.write(f"Score {0}",align="center" ,font=("Verdana", 15, "normal"))
        self.hideturtle()

    def increase(self):
        self.point=self.point+1
        self.clear()
        self.write(f"Score {self.point}", align="center", font=("Verdana", 15, "normal"))

    def gameover(self):
        self.goto((0,0))
        self.write(f"Game over", align="center", font=("Verdana", 15, "normal"))