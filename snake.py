from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        # square = Turtle('square')
        # square.color('white')
        square = Turtle('circle')
        square.color('Dark Green')
        square.shapesize(stretch_wid=0.7, stretch_len=0.7)
        # print(positions.index(i))
        # square.color(colors[positions.index(i)])
        square.penup()
        square.goto(position)
        self.segments.append(square)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        # self.head = self.segments[len(self.segments) - 1]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1): 
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
