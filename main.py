import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

game_on = True
x_border = 380
y_border = 290
x_screen = 600
y_screen = 810
game_over = False
game_border = False
screen = Screen()


def setup():
    print('in setup')
    setup_screen()
    # setup_borders()
    setup_objects()
    screen_listeners_set()


def setup_screen():
    print('in setup_screen')
    global screen
    screen.reset()
    screen = Screen()
    screen.setup(width=y_screen, height=x_screen)
    screen.bgcolor('Black')
    screen.title('5.2 Snake Game Day 20-21')
    screen.tracer(0)


def setup_borders():
    border = turtle.Turtle()
    border.hideturtle()
    border.penup()
    border.goto(x_border + 10, y_border)
    border.pensize(5)
    border.pendown()
    border.pencolor('gray')

    border.setheading(270)
    border.forward(x_screen - 25)

    border.setheading(180)
    border.forward(y_screen - 22)

    border.setheading(90)
    border.forward(x_screen - 25)

    border.setheading(0)
    border.forward(y_screen - 22)


def setup_objects():
    print('in setup_objects')
    global snake
    snake = Snake()
    global food
    food = Food()
    global score
    score = ScoreBoard()


def screen_listeners_set():
    print('in screen_listeners_set')
    global screen, snake
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(space, 'space')
    screen.onkey(reset, 'v')


def space():
    global game_on, game_over
    game_on = not game_on if not game_over else False
    gameplay()


def reset():
    global game_over, game_on
    if game_over:
        game_on = True
        game_over = False
        setup()
        gameplay()


def gameplay():
    print('in gameplay')
    global game_on
    global game_over
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()
            score.write_score()
            # print('Eaten')

        if game_border:
            if (snake.head.xcor() < -x_border or snake.head.xcor() > x_border or
                    snake.head.ycor() < -y_border or snake.head.ycor() > y_border):
                game_on = False
                game_over = True
                score.reset_score()
                # score.game_over()

        else:
            if snake.head.xcor() < -x_border or snake.head.xcor() > x_border:
                # x_temp=
                snake.head.goto(x=-snake.head.xcor(), y=snake.head.ycor())
            elif snake.head.ycor() < -y_border or snake.head.ycor() > y_border:
                # x_temp=
                snake.head.goto(x=snake.head.xcor(), y=-snake.head.ycor())

        for i in snake.segments[1:]:
            if snake.head.distance(i) < 10:
                game_on = False
                game_over = True
                score.reset_score()
                # score.game_over()


setup()
gameplay()
screen.exitonclick()
