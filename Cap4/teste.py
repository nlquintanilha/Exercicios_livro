#!/usr/bin/env python3
"""
Arquivo de teste para o módulo letters.py
Demonstra como usar as funções para desenhar letras e palavras
"""

import turtle
from letters import *

def main():
    """Função principal para demonstrar o uso do módulo letters"""
    
    # Configura a tela
    screen = turtle.Screen()
    screen.title("Teste do Alfabeto - Pense em Python 4.4")
    screen.bgcolor("white")
    screen.setup(width=1200, height=800)
    
    # Configura o turtle
    setup_turtle()
    
    print("Escolha uma opção:")
    print("1 - Desenhar uma letra específica")
    print("2 - Desenhar uma palavra")
    print("3 - Desenhar o alfabeto completo")
    print("4 - Desenhar exemplos de palavras")
    
    choice = input("Digite sua escolha (1-4): ")
    
    if choice == "1":
        # Desenhar uma letra específica
        letter = input("Digite uma letra (a-z): ").lower()
        if letter.isalpha() and len(letter) == 1:
            # Chama a função correspondente
            function_name = f"draw_{letter}"
            if function_name in globals():
                turtle.penup()
                turtle.goto(0, 0)
                turtle.pendown()
                globals()[function_name]()
            else:
                print(f"Função para a letra '{letter}' não encontrada!")
        else:
            print("Por favor, digite apenas uma letra válida!")
    
    elif choice == "2":
        # Desenhar uma palavra
        word = input("Digite uma palavra: ")
        draw_word(word)
    
    elif choice == "3":
        # Desenhar o alfabeto completo
        test_alphabet()
    
    elif choice == "4":
        # Desenhar exemplos de palavras
        examples = ["python", "turtle", "codigo", "letra"]
        
        for i, word in enumerate(examples):
            turtle.penup()
            turtle.goto(-len(word) * (LETTER_WIDTH + 20) // 2, 200 - i * 120)
            turtle.pendown()
            
            for letter in word.lower():
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
    
    else:
        print("Opção inválida!")
        return
    
    # Mantém a janela aberta
    print("Clique na janela do turtle para fechá-la...")
    screen.exitonclick()

if __name__ == "__main__":
    main()

draw_a()

draw_word("python")


