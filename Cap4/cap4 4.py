import turtle 
import math

def polygon(t, length, n):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(50 * angle / 360) 
    if n < 1:
        n = 1
    length = arc_length / n
    segment_angle = angle / n
    for _ in range(n):
        t.forward(length)
        t.left(segment_angle)   

def petals(t, r, angle):
    for _ in range(2):
        arc(t, r, angle)
        t.left(180 - angle)

def spiral(t, initial_length, angle, increment, n):  #increment: quanto aumentar o comprimento a cada passo
    length = initial_length
    for _ in range(n):
        t.forward(length)
        t.left(angle)
        length += increment

def rosette(t, shape_func, n, angle_increment, *args): #*agr: argumento para a função de forma
    for _ in range(n):
        shape_func(t, *args)
        t.left(angle_increment)


def star(t, size, n_points):  #n_points: número de pontas
   outer_angle = 360 / n_points
   inner_angle = 180 - outer_angle

   for _ in range(n_points):
        t.forward(size)
        t.left(inner_angle)
        t.forward(size)
        t.right(outer_angle)

bob = turtle.Turtle()
bob.speed(8)  

turtle.bgcolor("black")
bob.color("blue")

print ("desenhando padrões geometrico")

turtle.exitonclick()
