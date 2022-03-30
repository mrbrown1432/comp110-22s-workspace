from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.color("green", "yellow")
leo.penup()
leo.goto(-110, -100)
leo.pendown()
leo.pencolor("pink")
leo.fillcolor(38, 67, 93)
leo.end_fill
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1 

bob: Turtle = Turtle()
side_length: int = 300
side_length = side_length * 0.97

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(130)
    i = i + 1
done()