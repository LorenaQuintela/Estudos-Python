'''Coversão de Tempo
Um jogo possui 8.750 segundos de duração.
Descubra: 
- Quantas horas completas existem nesse período
- Quantos minutos completos sobram depois de retirar essas horas
- Quantos segundos sobram depois de retirar as horas e minutos.'''

# 1 hora 3.600 segundos 60min * 60seg
# 1 minuto possui 60 segundos

total_segundos = 8750

horas = total_segundos // 3600
resto_segundos = total_segundos % 3600

minutos = resto_segundos // 60
segundos = resto_segundos % 60

print(f"Horas completas {horas} horas.")
print(f"Minutos completos {minutos} minutos.")
print(f"Quantos segundos sobram depois de retirar as horas e minutos? {segundos}")

