from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.goto(-280, 210)
        self.write(f'Level: {self.level}', align='center', font=('Arial', 16, 'normal'))
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=('Arial', 16, 'normal'))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 16, 'normal'))