from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            x_position = 0.00
            y_position = 0.00
            turtle = Turtle(shape="circle")
            turtle.penup()
            turtle.color("gold", "green")
            turtle.shapesize(0.5, 0.5, 0.5)
            turtle.setposition(x_position, y_position)
            x_position += MOVE_DISTANCE
            self.snake.append(turtle)

    def move_up(self):
        if self.head.heading() != DOWN:  # self.head has self.snake[0] as the value where
            # self.snake[0] has the value from turtle, which created using Turtle()
            # which Turtle has the heading() function that we can use to find which direction its heading
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_snake(self):
        for part in range(len(self.snake) - 1, 0, -1):  # Len(snake) is the last turtle part
            # range(x, y, z) x: starting value | y: ending value | z: steps
            new_x_pos = self.snake[part - 1].xcor()
            new_y_pos = self.snake[part - 1].ycor()
            self.snake[part].goto(new_x_pos, new_y_pos)
        self.head.forward(MOVE_DISTANCE)
