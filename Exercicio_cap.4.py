import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Example")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Draw a square
for _ in range(4):
    t.forward(100)
    t.left(90)

# Wait for user to close the window
turtle.done()

#resolução do exercício 4.1
# Funções para desenhar formas geométricas com turtle

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)          

def polygon(t, n,nlength):
            angle = 360 / n
            for i in range(n):
                t.forward(nlength)
                t.left(angle)   

def circle(t, r):
    circumference = 2 * 3.14 * r
    n = 50
    length = circumference / n
    polygon(t, n, length) 
      
#exemplo de uso
bob = turtle.Turtle()
circle(bob, 100) 


