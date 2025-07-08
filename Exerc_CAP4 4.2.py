# Conjunto de funções que podem desenhar flores

import turtle 
import math

def polygon(t, length, n):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(50 * angle / 360)  
    if n < 1:
        n = 1
    length = arc_length / n
    segment_angle = angle / n
    for _ in range(n):
        t.forward(length)
        t.left(segment_angle)

def petal(t, r, angle):
    for _ in range(2):
        arc(t, r, angle)
        t.left(180 - angle)

def flower(t, n, r, angle):
    for _ in range(n):
        petal(t, r, angle)
        t.left(360 / n)

def move_turtle(t, distance):
    t.penup()
    t.forward(distance)
    t.pendown()

def turn_and_move(t, angle, distance):
   t.penup()
   t.left(angle)
   t.forward(distance)
   t.pendown()
     
def draw_stem(t, length):
    t.right(90)
    t.forward(length)
    t.left(90)
   
bob = turtle.Turtle()
bob.speed(5)

print ("desenhando flores...")

bob.color("red")
flower(bob, 6, 50, 60)

turn_and_move(bob, 0,150) #Mover para nova posição

bob.color("blue")
flower(bob, 8, 40, 45  )

turn_and_move(bob, 0, 150)

bob.color("purple")
flower(bob, 5, 60, 80)

turn_and_move(bob, -90, 150)
turn_and_move(bob, -90, 300)

bob.color("orange")
flower(bob, 12, 30, 30)

turn_and_move(bob, 0, 150)

bob.color("green")
flower(bob, 4, 70, 90)


turn_and_move(bob, 0, 150)  

bob.color("pink")
flower(bob, 7, 45, 70)

turn_and_move(bob, -90, 200)
turn_and_move(bob, -90, 200)

bob.color("red")
flower(bob, 6, 40, 60)

bob.color("darkgreen")
draw_stem(bob, 100) 

print("Desenho de flores concluído!")

turtle.done()

