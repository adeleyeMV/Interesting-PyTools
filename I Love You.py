import turtle

draw = turtle.Turtle()

def curve():
    draw.pen(pencolor="white", pensize=3, speed=5)
    for i in range(200):
        draw.rt(1)
        draw.fd(1)

def heart():
    draw.pen(pencolor="white",fillcolor="red", pensize=3, speed=5)
    draw.shape("turtle")
    draw.shapesize(1,1,1)
    draw.begin_fill()
    draw.lt(50)
    draw.fd(113)
    curve()
    draw.lt(120)
    curve()
    draw.fd(112)
    draw.end_fill()

    draw.hideturtle()


window = turtle.Screen()
window.bgcolor('black')

draw.penup()
draw.goto(-80,300)
draw.pendown()
draw.shapesize(1,2,1)

draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)

draw.begin_fill()

draw.fd(160)
draw.rt(90)
draw.fd(25)
draw.rt(90)
draw.fd(60)
draw.lt(90)

draw.fd(140)
draw.lt(90)
draw.fd(60)
draw.rt(90)
draw.fd(25)
draw.rt(90)
draw.fd(160)
draw.rt(90)
draw.fd(25)
draw.rt(90)
draw.fd(60)
draw.lt(90)
draw.fd(140)
draw.left(90)
draw.fd(60)
draw.rt(90)
draw.fd(25)

draw.end_fill()

draw.penup()
draw.goto(-550,-20)
draw.pendown()

draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=2)
draw.begin_fill()

draw.rt(90)
draw.fd(25)
draw.rt(90)
draw.fd(165)
draw.lt(90)
draw.fd(115)
draw.rt(90)
draw.fd(25)
draw.rt(90)
draw.fd(140)
draw.rt(90)
draw.fd(190)
draw.rt(90)

draw.end_fill()

draw.penup()
draw.fd(140)

draw.fd(70)

draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
draw.begin_fill()

draw.rt(90)
draw.fd(190)
draw.lt(90)
draw.pendown()
draw.circle(60)
draw.lt(90)
draw.penup()
draw.fd(20)
draw.rt(90)
draw.pendown()
draw.circle(40)
draw.rt(90)
draw.penup()
draw.fd(20)
draw.lt(90)

draw.end_fill()

draw.fd(100)
draw.pendown()

draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
draw.begin_fill()

draw.lt(100)
draw.fd(120)
draw.rt(100)
draw.fd(20)
draw.rt(80)
draw.fd(100)
draw.lt(80)
draw.fd(20)
draw.lt(80)
draw.fd(100)
draw.rt(80)
draw.fd(20)
draw.rt(100)
draw.fd(120)
draw.rt(80)
draw.fd(50)
draw.lt(180)

draw.end_fill()

draw.penup()
draw.fd(100)
draw.pendown()

draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
draw.begin_fill()

draw.lt(90)
draw.fd(120)
draw.rt(90)
draw.fd(80)
draw.rt(90)
draw.fd(20)
draw.rt(90)
draw.fd(60)
draw.lt(90)
draw.fd(30)
draw.lt(90)
draw.fd(60)
draw.rt(90)
draw.fd(20)
draw.rt(90)
draw.fd(60)
draw.lt(90)
draw.fd(30)
draw.lt(90)
draw.fd(60)
draw.rt(90)
draw.fd(20)
draw.rt(90)
draw.fd(80)

draw.end_fill()

draw.penup()
draw.rt(180)
draw.fd(200)
draw.pendown()


draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=2)
draw.begin_fill()

draw.lt(90)
draw.fd(50)
draw.lt(30)
draw.fd(80)
draw.rt(120)
draw.fd(20)
draw.rt(60)
draw.fd(60)
draw.lt(180)
draw.rt(60)
draw.fd(60)
draw.rt(60)
draw.fd(20)
draw.rt(120)
draw.fd(80)
draw.lt(30)
draw.fd(50)
draw.rt(90)
draw.fd(20)
draw.rt(180)

draw.end_fill()

draw.penup()
draw.fd(120)
draw.pendown()


draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
draw.begin_fill()

draw.circle(60)
draw.lt(90)
draw.penup()
draw.fd(20)
draw.pendown()
draw.rt(90)
draw.circle(40)
draw.rt(90)
draw.penup()
draw.fd(20)
draw.lt(90)

draw.end_fill()

draw.fd(100)
draw.circle(60, extent=60)
draw.pendown()

draw.pen(pencolor="white",fillcolor="yellow", pensize=3, speed=8)
draw.begin_fill()

draw.lt(30)

draw.fd(85)
draw.lt(90)
draw.fd(20)
draw.lt(90)
draw.fd(70)
draw.circle(-20, extent=180)
draw.fd(70)
draw.lt(90)

draw.fd(20)
draw.lt(90)
draw.fd(85)
draw.circle(40, extent=180)

draw.end_fill()

draw.penup()

draw.rt(180)
draw.fd(35)
draw.lt(90)
draw.fd(140)
draw.lt(90)
draw.pendown()

heart()

turtle.done()
#This code is contributed by Shivesh Shivam
