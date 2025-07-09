import turtle
import math

# Configurações globais
LETTER_SIZE = 100
LETTER_WIDTH = 60

def setup_turtle():
    """Configura o turtle para desenhar letras"""
    turtle.speed(0)
    turtle.pensize(3)
    turtle.color('black')

def move_to_start():
    """Move o turtle para a posição inicial da letra"""
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, -LETTER_SIZE//2)
    turtle.pendown()

def move_to_next_letter():
    """Move o turtle para a próxima posição de letra"""
    turtle.penup()
    turtle.forward(LETTER_WIDTH + 20)
    turtle.pendown()

# Elementos básicos para construir letras
def draw_vertical_line(height=LETTER_SIZE):
    """Desenha uma linha vertical"""
    turtle.setheading(90)  # Aponta para cima
    turtle.forward(height)

def draw_horizontal_line(width=LETTER_WIDTH):
    """Desenha uma linha horizontal"""
    turtle.setheading(0)  # Aponta para a direita
    turtle.forward(width)

def draw_diagonal_right(length=None):
    """Desenha uma diagonal para a direita"""
    if length is None:
        length = math.sqrt(LETTER_WIDTH**2 + LETTER_SIZE**2)
    angle = math.degrees(math.atan(LETTER_SIZE / LETTER_WIDTH))
    turtle.setheading(angle)
    turtle.forward(length)

def draw_diagonal_left(length=None):
    """Desenha uma diagonal para a esquerda"""
    if length is None:
        length = math.sqrt(LETTER_WIDTH**2 + LETTER_SIZE**2)
    angle = 180 - math.degrees(math.atan(LETTER_SIZE / LETTER_WIDTH))
    turtle.setheading(angle)
    turtle.forward(length)

def draw_semicircle(radius, direction=1):
    """Desenha um semicírculo (direction: 1 para direita, -1 para esquerda)"""
    turtle.circle(radius, 180 * direction)

def draw_quarter_circle(radius, direction=1):
    """Desenha um quarto de círculo"""
    turtle.circle(radius, 90 * direction)

# Funções para desenhar cada letra
def draw_a():
    """Desenha a letra A"""
    move_to_start()
    # Linha esquerda
    turtle.setheading(75)
    turtle.forward(LETTER_SIZE)
    # Linha direita
    turtle.backward(LETTER_SIZE)
    turtle.setheading(105)
    turtle.forward(LETTER_SIZE)
    # Barra horizontal
    turtle.backward(LETTER_SIZE * 0.4)
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.6)

def draw_b():
    """Desenha a letra B"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Volta para baixo
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE)
    # Linha horizontal inferior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.7)
    # Semicírculo inferior
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//4, 180)
    # Linha horizontal do meio
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH * 0.7)
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.7)
    # Semicírculo superior
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//4, 180)
    # Linha horizontal superior
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH * 0.7)

def draw_c():
    """Desenha a letra C"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2 + LETTER_WIDTH, -LETTER_SIZE//2)
    turtle.pendown()
    # Semicírculo
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//2, 180)

def draw_d():
    """Desenha a letra D"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Volta para baixo
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE)
    # Linha horizontal inferior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.5)
    # Semicírculo direito
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//2, 180)
    # Linha horizontal superior
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH * 0.5)

def draw_e():
    """Desenha a letra E"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Linha horizontal superior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)
    # Volta para a linha do meio
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH)
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Linha horizontal do meio
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.8)
    # Volta para baixo
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH * 0.8)
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Linha horizontal inferior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)

def draw_f():
    """Desenha a letra F"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Linha horizontal superior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)
    # Volta para a linha do meio
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH)
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Linha horizontal do meio
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.8)

def draw_g():
    """Desenha a letra G"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2 + LETTER_WIDTH, -LETTER_SIZE//2)
    turtle.pendown()
    # Semicírculo
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//2, 180)
    # Linha horizontal do meio
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.5)
    # Linha vertical pequena
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//4)

def draw_h():
    """Desenha a letra H"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Vai para o meio
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Linha horizontal do meio
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)
    # Linha vertical direita (parte superior)
    turtle.setheading(90)
    turtle.forward(LETTER_SIZE//2)
    # Linha vertical direita (parte inferior)
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE)

def draw_i():
    """Desenha a letra I"""
    move_to_start()
    # Linha horizontal inferior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)
    # Vai para o meio
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH//2)
    # Linha vertical central
    turtle.setheading(90)
    turtle.forward(LETTER_SIZE)
    # Linha horizontal superior
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH//2)
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)

def draw_j():
    """Desenha a letra J"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Linha horizontal superior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)
    # Vai para o meio
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH//2)
    # Linha vertical
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE * 0.8)
    # Curva inferior
    turtle.setheading(180)
    turtle.circle(LETTER_SIZE//8, 180)

def draw_k():
    """Desenha a letra K"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Vai para o meio
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Diagonal superior
    turtle.setheading(45)
    turtle.forward(LETTER_SIZE//2 * 1.4)
    # Volta para o meio
    turtle.setheading(225)
    turtle.forward(LETTER_SIZE//2 * 1.4)
    # Diagonal inferior
    turtle.setheading(315)
    turtle.forward(LETTER_SIZE//2 * 1.4)

def draw_l():
    """Desenha a letra L"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Volta para baixo
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE)
    # Linha horizontal inferior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)

def draw_m():
    """Desenha a letra M"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Diagonal para o meio
    turtle.setheading(315)
    turtle.forward(LETTER_SIZE//2 * 1.4)
    # Diagonal para a direita
    turtle.setheading(45)
    turtle.forward(LETTER_SIZE//2 * 1.4)
    # Linha vertical direita
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE)

def draw_n():
    """Desenha a letra N"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Diagonal
    turtle.setheading(315)
    turtle.forward(LETTER_SIZE * 1.4)
    # Linha vertical direita
    turtle.setheading(90)
    turtle.forward(LETTER_SIZE)

def draw_o():
    """Desenha a letra O"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2 + LETTER_WIDTH//2, -LETTER_SIZE//2)
    turtle.pendown()
    # Círculo
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//2)

def draw_p():
    """Desenha a letra P"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Volta para baixo até o meio
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Linha horizontal do meio
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.7)
    # Semicírculo superior
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//4, 180)
    # Linha horizontal superior
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH * 0.7)

def draw_q():
    """Desenha a letra Q"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2 + LETTER_WIDTH//2, -LETTER_SIZE//2)
    turtle.pendown()
    # Círculo
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//2)
    # Linha diagonal no canto inferior direito
    turtle.penup()
    turtle.goto(LETTER_WIDTH//4, -LETTER_SIZE//4)
    turtle.pendown()
    turtle.setheading(315)
    turtle.forward(LETTER_SIZE//4)

def draw_r():
    """Desenha a letra R"""
    move_to_start()
    # Linha vertical esquerda
    draw_vertical_line()
    # Volta para baixo até o meio
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Linha horizontal do meio
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH * 0.7)
    # Diagonal inferior
    turtle.setheading(315)
    turtle.forward(LETTER_SIZE//2 * 1.4)
    # Volta para o meio
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2 + LETTER_WIDTH * 0.7, 0)
    turtle.pendown()
    # Semicírculo superior
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//4, 180)
    # Linha horizontal superior
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH * 0.7)

def draw_s():
    """Desenha a letra S"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2 + LETTER_WIDTH, -LETTER_SIZE//2 + LETTER_SIZE//4)
    turtle.pendown()
    # Semicírculo inferior
    turtle.setheading(90)
    turtle.circle(LETTER_SIZE//4, 180)
    # Semicírculo superior
    turtle.circle(-LETTER_SIZE//4, 180)

def draw_t():
    """Desenha a letra T"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Linha horizontal superior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)
    # Vai para o meio
    turtle.setheading(180)
    turtle.forward(LETTER_WIDTH//2)
    # Linha vertical central
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE)

def draw_u():
    """Desenha a letra U"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Linha vertical esquerda
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE * 0.75)
    # Semicírculo inferior
    turtle.setheading(0)
    turtle.circle(LETTER_WIDTH//4, 180)
    # Linha vertical direita
    turtle.setheading(90)
    turtle.forward(LETTER_SIZE * 0.75)

def draw_v():
    """Desenha a letra V"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Linha diagonal esquerda
    turtle.setheading(285)
    turtle.forward(LETTER_SIZE * 1.1)
    # Linha diagonal direita
    turtle.setheading(75)
    turtle.forward(LETTER_SIZE * 1.1)

def draw_w():
    """Desenha a letra W"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Linha diagonal esquerda
    turtle.setheading(285)
    turtle.forward(LETTER_SIZE * 1.1)
    # Linha diagonal para o meio
    turtle.setheading(75)
    turtle.forward(LETTER_SIZE//2 * 1.1)
    # Linha diagonal para baixo
    turtle.setheading(285)
    turtle.forward(LETTER_SIZE//2 * 1.1)
    # Linha diagonal direita
    turtle.setheading(75)
    turtle.forward(LETTER_SIZE * 1.1)

def draw_x():
    """Desenha a letra X"""
    move_to_start()
    # Diagonal da esquerda inferior para direita superior
    turtle.setheading(45)
    turtle.forward(LETTER_SIZE * 1.4)
    # Vai para o canto superior esquerdo
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Diagonal da esquerda superior para direita inferior
    turtle.setheading(315)
    turtle.forward(LETTER_SIZE * 1.4)

def draw_y():
    """Desenha a letra Y"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Linha diagonal esquerda para o meio
    turtle.setheading(315)
    turtle.forward(LETTER_SIZE//2 * 1.4)
    # Linha vertical para baixo
    turtle.setheading(270)
    turtle.forward(LETTER_SIZE//2)
    # Volta para o meio
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    # Linha diagonal direita
    turtle.setheading(45)
    turtle.forward(LETTER_SIZE//2 * 1.4)

def draw_z():
    """Desenha a letra Z"""
    move_to_start()
    turtle.penup()
    turtle.goto(-LETTER_WIDTH//2, LETTER_SIZE//2)
    turtle.pendown()
    # Linha horizontal superior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)
    # Linha diagonal
    turtle.setheading(225)
    turtle.forward(LETTER_SIZE * 1.4)
    # Linha horizontal inferior
    turtle.setheading(0)
    turtle.forward(LETTER_WIDTH)

def draw_space():
    """Desenha um espaço (apenas move o turtle)"""
    turtle.penup()
    turtle.forward(LETTER_WIDTH)
    turtle.pendown()

# Função para desenhar uma palavra
def draw_word(word):
    """Desenha uma palavra usando as funções de letras"""
    letter_functions = {
        'a': draw_a, 'b': draw_b, 'c': draw_c, 'd': draw_d, 'e': draw_e,
        'f': draw_f, 'g': draw_g, 'h': draw_h, 'i': draw_i, 'j': draw_j,
        'k': draw_k, 'l': draw_l, 'm': draw_m, 'n': draw_n, 'o': draw_o,
        'p': draw_p, 'q': draw_q, 'r': draw_r, 's': draw_s, 't': draw_t,
        'u': draw_u, 'v': draw_v, 'w': draw_w, 'x': draw_x, 'y': draw_y,
        'z': draw_z, ' ': draw_space
    }
    
    # Posiciona o turtle no início
    turtle.penup()
    turtle.goto(-len(word) * (LETTER_WIDTH + 20) // 2, 0)
    turtle.pendown()
    
    for letter in word.lower():
        if letter in letter_functions:
            letter_functions[letter]()
            move_to_next_letter()

# Função de teste
def test_alphabet():
    """Testa todas as letras do alfabeto"""
    setup_turtle()
    
    # Desenha o alfabeto completo
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Divide em 3 linhas
    lines = ["abcdefghi", "jklmnopqr", "stuvwxyz"]
    
    start_y = 150
    for i, line in enumerate(lines):
        turtle.penup()
        turtle.goto(-len(line) * (LETTER_WIDTH + 20) // 2, start_y - i * 150)
        turtle.pendown()
        
        for letter in line:
            if letter == 'a':
                draw_a()
            elif letter == 'b':
                draw_b()
            elif letter == 'c':
                draw_c()
            elif letter == 'd':
                draw_d()
            elif letter == 'e':
                draw_e()
            elif letter == 'f':
                draw_f()
            elif letter == 'g':
                draw_g()
            elif letter == 'h':
                draw_h()
            elif letter == 'i':
                draw_i()
            elif letter == 'j':
                draw_j()
            elif letter == 'k':
                draw_k()
            elif letter == 'l':
                draw_l()
            elif letter == 'm':
                draw_m()
            elif letter == 'n':
                draw_n()
            elif letter == 'o':
                draw_o()
            elif letter == 'p':
                draw_p()
            elif letter == 'q':
                draw_q()
            elif letter == 'r':
                draw_r()
            elif letter == 's':
                draw_s()
            elif letter == 't':
                draw_t()
            elif letter == 'u':
                draw_u()
            elif letter == 'v':
                draw_v()
            elif letter == 'w':
                draw_w()
            elif letter == 'x':
                draw_x()
            elif letter == 'y':
                draw_y()
            elif letter == 'z':
                draw_z()
            
            move_to_next_letter()

# Exemplo de uso
if __name__ == "__main__":
    setup_turtle()
    
    # Teste individual de uma letra
    # draw_a()
    
    # Teste de uma palavra
    # draw_word("python")
    
    # Teste do alfabeto completo
    test_alphabet()
    
    # Mantém a janela aberta
    turtle.done()