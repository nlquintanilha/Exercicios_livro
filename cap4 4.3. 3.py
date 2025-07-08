#teste
import turtle
import math 

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
                         
def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.right(angle)

def circle(t, r): 
    circumference = 2 * math.pi * r
    n = 50  # Número de segmentos para aproximar o círculo
    length = circumference / n

    for i in range(n):
        t.forward(length)
        t.right(360 / n)
    polygon(t, length, n)


bob = turtle.Turtle()


circle(bob, 20)  # Círculo pequeno com raio 20
bob.penup() 
bob.goto(100, 0)
bob.pendown()

circle(bob, 30)  # Círculo médio com raio 30
bob.penup() 
bob.goto(200, 0)
bob.pendown()

circle(bob, 40)  # Círculo grande com raio 40
bob.penup() 
bob.goto(0, -150)
bob.pendown()

circle(bob, 50)  # Círculo maior com raio 50
bob.penup() 
bob.goto(150, -150)
bob.pendown()   

bob.color("red")
circle(bob, 35 )        # Círculo vermelho com raio 35

bob.penup()
bob.goto(300, 0)    
bob.pendown()
bob.color("blue")
polygon(bob, 36, 6)  

turtle.done()




