# from asyncore import write
# from tkinter import font
import turtle

wind = turtle.Screen()  # initialize screen
wind.title('ping pong by Jemy')  # title of window
wind.bgcolor("black")  # background window
wind.setup(width=800, height=600)  # width and height window
wind.tracer(0)

# madrab1
madrab1 = turtle.Turtle()  # madarb1 shape
madrab1.speed(0)
madrab1.shape("square")  # madarb1 shape
madrab1.color("red")  # madrab1 color
madrab1.shapesize(stretch_wid=5, stretch_len=0.5)  # width and height madrab1
madrab1.penup()
madrab1.goto(-380, 0)  # place madarb1
# madrab2 turtle
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("blue")
madrab2.shapesize(stretch_wid=5, stretch_len=0.5)
madrab2.penup()
madrab2.goto(380, 0)

# ball turtle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")  # ball shape
ball.color("white")  # ball color
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)  # width and height ball
ball.penup()
ball.goto(0, 0)  # initialization place ball
ball.dx = 0.5
ball.dy = 0.5

# score
score1 = 0  # initial score player 1=0
score2 = 0  # initial score player 2=0
score = turtle.Turtle()  # score turtle
score.speed(0)
score.color("white")  # score color
score.penup()
score.hideturtle()
score.goto(0, 260)  # place of score
score.write("player 1:{} player 2: {}".format(score1, score2), align="center",
            font=("courier", 24, "normal"))
# final window
fwind = turtle.Turtle()
fwind.speed(0)
fwind.penup()


# function1
def madrab1_up():
    y = madrab1.ycor()  # move madrab1 on Y-axis up
    y += 20  # move by 20 pixel
    madrab1.sety(y)


def madrab1_botton():
    y = madrab1.ycor()  # move madrab1 on Y-axis down
    y += -20  # move by 20 pixel
    madrab1.sety(y)


# keyboard1
wind.listen()
wind.onkeypress(madrab1_up, "w")  # move madrab1 to up py botton 'w'
wind.onkeypress(madrab1_botton, "s")  # move madrab1 to down by botton 's'


# function2


def madrab2_up():
    y = madrab2.ycor()  # move madrab2 on Y-Axis to up
    y += 20  # move madrab2 py 20 pixel
    madrab2.sety(y)


def madrab2_botton():
    y = madrab2.ycor()  # move madrab2 on Y-Axis to down
    y += -20  # move madrab2 py 20 pixel
    madrab2.sety(y)


# keyboard2
wind.listen()
wind.onkeypress(madrab2_up, "Up")  # move madrab2 to up by botton 'UP'
# move madrab2 to down by botton 'Down'
wind.onkeypress(madrab2_botton, "Down")

# function to move the ball


while True:
    wind.update()  # loop of all application

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # order check
    if ball.ycor() > 290:
        # when the ball heat in the Y wall in quarter 1 & 2 it will come back
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        # when the ball heat in the Y wall in quarter 3 & 4 it will come back
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        # when the ball heat in the X wall in quarter 1 & 2 it will come back
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2),
                    align="center", font=("courier", 24, "normal"))
        if score1 == 10:
            fwind.color("white")  # color of words
            fwind.penup()
            fwind.write("player1 is win", align="center", font=(
                "courier", 24, "normal"))  # the title it will show
            # when player2 scored 10 point
            fwind.goto(0, 0)
            score2 = 0
            ball.goto(0, 0)  # the ball will go to point (0, 0)
            ball.dx *= 0  # and ball.dx will be = 0

    if ball.xcor() < -390:
        # when the ball heat in the X wall in quarter 3 & 4 it will come back
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2),
                    align="center", font=("courier", 24, "normal"))
        if score2 == 10:  # when player2 score 10 point... window will show and say player2 is won
            fwind.color("white")  # color of words
            fwind.penup()
            fwind.write("player2 is win", align="center", font=(
                "courier", 24, "normal"))  # the title it will show
            # when player2 scored 10 point
            fwind.goto(0, 0)
            score1 = 0
            ball.goto(0, 0)  # the ball will go to point (0, 0)
            ball.dx *= 0  # and ball.dx will be = 0

    # stardom madrab and ball
    if (370 < ball.xcor() < 380) and (
            madrab2.ycor() + 60 > ball.ycor() > madrab2.ycor() - 60):
        ball.setx(360)
        ball.dx *= -1  # when ball heat in madrab1 it will come back in another way

    if (-370 > ball.xcor() > -380) and (
            madrab1.ycor() + 60 > ball.ycor() > madrab1.ycor() - 60):
        ball.setx(-360)
        ball.dx *= -1  # when ball heat in madrab2 it will come back in another ways
