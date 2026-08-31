'''Uma viagem começou as 07:35  e terminou as 11:20
Descubra quanto tempo durou a viagem, em horas e minutos'''


'''1 - Completar hora (7:35 até 8:00)
-subtração: 60 - 35 = 25
-Faltam 25 minutos para as 8:00
2 - Contas as horas ( 8:00 até 11:00)
- Subtração: 11 - 8 = 3 
- Temos 3 horas exatas.
- Somar os minutos = 25 que faltava para completar as 8 hrs e os 20 min que tem nas 11 hrs -> 25 + 20 = 45 
-Total = 3:45 '''


hora_inicio, min_inicio = 7, 35 
hora_fim, min_fim = 11, 20

total_min_inicio = (hora_inicio * 60) + min_inicio # 455
total_min_fim = (hora_fim * 60) + min_fim # 680

diferenca_minutos = total_min_fim - total_min_inicio # 225

duracao_horas = diferenca_minutos // 60 
duracao_minutos = diferenca_minutos % 60

print(f"A viagem durou {duracao_horas} horas e {duracao_minutos} minutos.")