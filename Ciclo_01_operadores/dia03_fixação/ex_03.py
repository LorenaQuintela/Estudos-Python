'''Uma pessoa recebe R$ 3.200 por mês. Seus gastos são: 
- Aluguel: R$ 1.100
- Alimentação: R$ 550
- Transporte: R$ 280
- Internet: R$ 120
- Lazer: R$ 250
Depois de pagar todos os gastos, ela decide: 
- Guardar 25% do valor que sobrou
- Usar o restante para outras despesas
Descubra: 
- Total gasto no mês? Quanto sobrou depois dos gastos? Quanto será guardado? Quanto ficará disponível para outras despesas? '''
salario = 3200
aluguel = 1100
alimentacao = 550
transporte = 280
internet = 120
lazer = 250

porcentagem = 25

total_gasto = aluguel + alimentacao + transporte + internet + lazer
total_apos_gastos = salario - total_gasto

valor_guardado = total_apos_gastos * porcentagem / 100
disponivel_para_despesas = total_apos_gastos - valor_guardado

print(f"Total gasto no mês?  {total_gasto:.2f}")
print(f"Quanto sobrou depois dos gastos? {total_apos_gastos:.2f}")
print(f"Quanto será guardado? {valor_guardado:.2f}")
print(f"Quanto ficará disponível para outras despesas? {disponivel_para_despesas:.2f}")