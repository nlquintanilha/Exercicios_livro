import turtle

# exercícos 4.1 com Tratamento de Exceções

def square (t):
    try: 
        if not isinstance(t, turtle.Turtle):
              raise TypeError("O parâmetro deve ser uma instância de turtle.Turtle.")   
        for i in range(4):
                t.forward(100)
                t.left(90)  
    except TypeError as e:
            print(f"Erro de tipo na função square: {e}")
    except Exception as e:
            print(f"Ocorreu um erro inesperado na função square: {e}")  
        
def polygon(t, n, nlength):
    try:
        if not isinstance(t, turtle.Turtle): #Garantir que o primeiro parâmetro seja realmente uma tartaruga válida.
            raise TypeError("O parâmetro deve ser uma instância de turtle.Turtle.")
        if n <= 0 or nlength <= 0:
            raise ValueError("O número de lados e o comprimento devem ser positivos.")
        angle = 360 / n
        for i in range(n):
            t.forward(nlength)
            t.left(angle)
    except TypeError as e:
        print(f"Erro de tipo na função polygon: {e}")
    except ValueError as e:
        print(f"Erro de valor na função polygon: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado na função polygon: {e}") 

def circle(t, r):
    try:
        if not isinstance(t, turtle.Turtle):
             raise TypeError("O parâmetro deve ser uma instância de turtle.Turtle.")
        if r <= 0: 
            raise ValueError("O raio deve ser positivo.")
        circumference = 2 * 3.14 * r    
        n = 50
        length = circumference / n
        polygon(t, n, length)
    except TypeError as e:
         print(f"Erro de tipo na função circle: {e}")
    except ValueError as e: 
         print(f"Erro de valor na função circle: {e}")  
    except Exception as e:
         print(f"Ocorreu um erro inesperado na função circle: {e}")

    def main():
        try:
              bob = turtle.Turtle()
              square(bob)
              polygon(bob, 5, 70)
              circle(bob, 100)
              turtle.done() 
        except Exception as e:
            print(f"Ocorreu um erro inesperado no main: {e}")
        
        finally:
            try:
                    turtle.bye()  # Fecha a janela do turtle
            except turtle.Terminator:
                    print("A janela do turtle já foi fechada.")
            except Exception as e:
                    print(f"Ocorreu um erro ao fechar a janela do turtle: {e}") 
        
    main()
       
  