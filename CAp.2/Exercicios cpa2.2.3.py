from datetime import datetime, timedelta

def calcular_passo_e_velocidade(distancia_km, tempo_minutos, tempo_segundos):
     
     try: 
          hora_saida = datetime.strptime("06:00", "%H:%M")
          except ValueError as e: 
            raise ValueError("Formato de hora inválido. Use HH:MM.")
     
     #dados da corrida

     try:
         #primeiro trecho: 1km a 8min15s por km

         ditancia_1 = 1
         passo_1_min = 8
        passo_1_seg = 15
     tempo_1_total_seg = (passo_1_min * 60) + passo_1_seg

     #segundo trecho: 3km a7min12s por km
     distancia_2 = 3
        passo_2_min = 7
        passo_2_seg = 12
     tempo_2_total_seg = (passo_2_min * 60) + passo_2_seg

     tempo_2_total_seg = tempo_2_total_seg * distancia_2

     #terceiro trecho 1kim no memso passo do primeiro trecho
        distancia_3 = 1
     tempo_3_total_seg = tempo_1_total_seg 

     except Exception as e:
         raise ValueError("Erro ao calcular os trechos da corrida. Verifique os valores de entrada.")   

try: 
    tempo_1 = timedelta(seconds=tempo_1_total_seg
tempo_2 = timedelta(seconds=tempo_2_total_seg)
tempo_3 = timedelta(seconds=tempo_3_total_seg)

except Exception as e:
    raise ValueError("Erro ao calcular os tempos dos trechos. Verifique os valores de entrada.")    

    try: 
    tempo_total_corrida = tempo_1 + tempo_2 + tempo_3
    ditancia_total_km = distancia_1 + distancia_2 + distancia_3
    except Exception as e:
        raise ValueError("Erro ao calcular o tempo total da corrida. Verifique os valores de entrada.") 

        try: 
        horario_chegada = hora_saida + tempo_total_corrida
        except Exception as e:
            raise ValueError("Erro ao calcular o horário de chegada. Verifique os valores de entrada.") 

            print (f"\n RESULTADO FINAL:")
            print(f"Chegada: {horario_chegada.strftime('%H:%M')}")
            print(f"Distância total: {distancia_total_km} km")
            print(f"Tempo total: {tempo_total_corrida}")
            print(f"Passo médio: {tempo_total_corrida / distancia_total_km}")
            print(f"Velocidade média: {distancia_total_km / (tempo_total_corrida.total_seconds() / 3600)} km/h")

    except ValueError as e:
        print(f"Erro: {e}") 

        