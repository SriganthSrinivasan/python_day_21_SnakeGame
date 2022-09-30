from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.setposition(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.setposition(0.00, 0.00)
        self.write(f"Game Over.", move=False, align=ALIGNMENT,
                   font=FONT)

    def new_score(self):
        self.clear()
        self.score += 1
        self.update_score()
