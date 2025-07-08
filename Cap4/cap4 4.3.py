#teste
import turtle

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
                         
def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.right(angle)

bob = turtle.Turtle()

polygon(bob, 50, 3)  # Triângulo

bob.penup()
bob.goto(100, 0)
bob.pendown()

polygon(bob, 60, 5)  # Pentágono
bob.penup()
bob.goto(200, 0)
bob.pendown()

polygon(bob, 50, 6)  # Hexágono
bob.penup()
bob.goto(0, -150)
bob.pendown()

polygon(bob, 40, 8)  # Octógono
bob.penup()
bob.goto(150, -150)
bob.pendown()

polygon(bob, 30, 12)  # Dodecágono
bob.penup()
bob.goto(300, 0)
bob.pendown()

square (bob, 80)  # Quadrado

turtle.done()



