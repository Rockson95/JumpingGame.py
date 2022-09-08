#Building a pong game
#It is a two dimentional game that simulate table tennis.
#The player controls an in-game by paddle by moving it vertically accross left or rigt on the screen.
#The player use the paddle to hit the ball back and forth.

#turtle which is my murgle name
import turtle
window = turtle.Screen()
window.title("Jumping(Pong) Game created by Rockson Adjah-Tettheh")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#Score
score_a =0
score_b = 0

#Now let create our paddle

###Paddle A
#Turtle() is my class name
paddle_a = turtle.Turtle()
#This not a speed of the game. It is a speed of the animation
paddle_a.speed(0)
#Paddle shape(sqaure, triange,circle)
paddle_a.shape("square")
#Paddle A color
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=7, stretch_len=0.5)
#Pen up means i dont need any line drawn
paddle_a.penup()
# Paddle A gotto means, the axis of the paddle. zero is at the centre
paddle_a.goto(-350,0)

###Paddle B
#Turtle() is my class name
paddle_b = turtle.Turtle()
#This not a speed of the game. It is a speed of the animation
paddle_b.speed(0)
#Paddle shape(sqaure, triange,circle)
paddle_b.shape("square")
#Paddle A color
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=7, stretch_len=0.5)
#Pen up means i dont need any line drawn
paddle_b.penup()
# Paddle A gotto means, the axis of the paddle. zero is at the centre
paddle_b.goto(350,0)

###The ball
#Turtle() is my class name
ball = turtle.Turtle()
#This not a speed of the game. It is a speed of the animation
ball.speed(0)
#Paddle shape(sqaure, triange,circle)
ball.shape("circle")
#ball A color
ball.color("red")
#Pen up means i dont need any line drawn
ball.penup()
# Paddle A gotto means, the axis of the paddle. zero is at the centre
ball.goto(0,0)
ball.dx=0.2
ball.dy=-0.2

#Using turtle module pen for the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player Rock: 0  Player Adjah:0", align="center", font=("courier", 24, "normal"))

###Fucntion: A function is a piece of program that has been defined for
#To use a fuction you need to define a function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
            y = paddle_b.ycor()
            y += 20
            paddle_b.sety(y)

def paddle_b_down():
            y = paddle_b.ycor()
            y -= 20
            paddle_b.sety(y)

##A keyboard binding
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")

window.onkeypress(paddle_b_up,"i")
window.onkeypress(paddle_b_down,"k")


### Main game loop. what is mean is that anytime the loop runs it update the screen
while True:
    window.update()
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ball.dy)

 #Border checking
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player Rock: {}  Player Adjah:{}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
       ball.goto(0, 0)
       ball.dx *= -1
       score_b +=1
       pen.clear()
       pen.write("Player Rock: {}  Player Adjah:{}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))


  #Paddle and ball collision
    if (ball.xcor()>340 and ball.xcor() >- 350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor() -40):
       ball.setx(340)
       ball.dx *=-2

    if (ball.xcor()<-340 and ball.xcor() < 350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() -40):
       ball.setx(340)
       ball.dx *=-2