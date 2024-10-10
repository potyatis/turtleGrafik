import turtle
primes = [2]
number = 2
for i in range(5000):
    number +=1
    for prime in primes:
        if number%prime == 0:
            break
        elif prime < number**(1/2):
            continue
        else:
            primes.append(number)
            break
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("grey")
turtle.width(2)
t.color("white")
for prime in primes:
    t.forward(prime**(1/2))
    t.right(prime)
turtle.done()
screen.exitonclick()