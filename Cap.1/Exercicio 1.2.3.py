# Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?
 
def calcular_passo_e_velocidade(distancia_km, tempo_minutos, tempo_segundos):
   '''
    Calcula o passo médio e a velocidade média a partir da distância e tempo
    '''
   try: 
      if distancia_km <= 0 or tempo_minutos < 0 or tempo_segundos < 0:
            raise ValueError("Distância e tempo devem ser positivos.")
