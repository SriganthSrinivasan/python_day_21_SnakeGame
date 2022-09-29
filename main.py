from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.title("Welcome to Snake Game 🐍")
screen.setup(width=600, height=600)
screen.bgpic("snake_bg.gif")
screen.textinput(title="Snake Game", prompt="Enter your name")
screen.tracer(0)  # Making the animation changes tracing 'off'
# So that you can see a flawless movement in the output console

snake = Snake()
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")

game_over = False
while not game_over:
    screen.update()  # Important part of screen.tracer() usage is using screen.update()
    # You can use this update in different location, which will update accordingly
    time.sleep(0.1)  # This will control the speed of execution by 0.2 second
    # Now we will have 0.2 sec sleep after whole for loop execution
    snake.move_snake()


screen.exitonclick()
