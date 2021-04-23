from turtle import *
screen = Screen()
pen = Turtle()
pen.color('black')
pen.fillcolor('red')
pen.begin_fill()
for i in range(5):
    pen.forward(300)
    pen.left(144)
pen.end_fill()
screen.exit.click()