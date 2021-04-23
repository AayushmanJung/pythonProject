import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
pen.speed(100)
def drawCircle(x,y,r):
    pen.pu()
    pen.goto(x,y-r)
    pen.pd()
    pen.circle(r)
def makePictures(r):
    if r<20:
        pass
    else:
        drawCircle(0,0,r)
        makePictures(r-20)
makePictures(200)
turtle.done()