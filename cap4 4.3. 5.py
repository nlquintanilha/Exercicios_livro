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

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    arc_length = circumference * (angle / 360)
    n = int(50* (angle / 360))  # Número de segmentos para o arco
    if n < 1:
        n = 1
    length = arc_length / n
    segment_angle = angle / n
    for i in range(n):
        t.forward(length)
        t.right(segment_angle)
        
bob = turtle.Turtle()

arc(bob, 50, 90)  # Arco com raio 50 e ângulo de 90 graus

bob.penup()
bob.goto(150, 0)
bob.pendown()

arc(bob, 40, 180)  # Arco com raio 40 e ângulo de 180 graus

bob.penup()
bob.goto(0, -120)
bob.pendown()

arc(bob, 30, 270)  # Arco com raio 30 e ângulo de 270 graus 
bob.penup()
bob.goto(150, -120) 
bob.pendown()

arc(bob, 30, 360)  # Arco completo com raio 30  
bob.penup()
bob.goto(300, 0)    
bob.pendown()

arc(bob, 25, 45)  # Arco com raio 25 e ângulo de 45 graus
bob.penup()
bob.goto(300, -60  )
bob.pendown()

bob.color("red")
arc(bob, 40, 360)  # Arco com raio 20 e

bob.penup()
bob.goto(100, -250) 
bob.pendown()
bob.color("blue")
circle (bob,40)

  # Arco com raio 50 e ângulo de 180 graus

turtle.done()




