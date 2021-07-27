import turtle
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
flag=True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food)<15):
        food.set_position()
        score.increase()
        snake.eat()

    if(snake.head.xcor() > 370 or snake.head.xcor()<-370 or snake.head.ycor()<-320 or snake.head.ycor()>320):
        flag=False
        score.gameover()

    for segment in snake.segments[1:]:


        if(snake.head.distance(segment)<10):
            print(snake.head.distance(segment))
            score.gameover()
            flag=False



screen.exitonclick()