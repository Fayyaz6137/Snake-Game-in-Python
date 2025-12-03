from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt', mode='r') as file:
            self.highest_score = int(file.read())
        self.write_score()

    def get_score(self):
        return self.score

    def increase_score(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.write(arg=f'Score : {self.score} High Score : {self.highest_score}', move=False, align=ALIGNMENT,
                   font=FONT)

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!\nPress Enter to try again.', move=False, align=ALIGNMENT, font=FONT)
