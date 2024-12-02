import turtle
import random

#setup
screen = turtle.Screen()
screen.setup(1000,800)
screen.bgcolor("#000000")
n = int(input("hur många taggar vill du ha"))
t = turtle.Turtle()
t.color("white","yellow")
t.width(2)
t.speed(0)

def draw_star(t_obj : turtle,x, y, size):
    angle = 120
    t_obj.penup()
    t_obj.goto(x,y)
    t_obj.pendown()
    t_obj.begin_fill()  
    for _ in range(n):
        t_obj.forward(size)
        t_obj.right(angle)
        t_obj.forward(size)
        t_obj.right((360/n) - angle)
    t.end_fill()

for _ in range(50):
    x, y = random.randint(-400,400), random.randint(-350,350)
    draw_star(t,x,y,random.randint(10,20))

screen.exitonclick()
