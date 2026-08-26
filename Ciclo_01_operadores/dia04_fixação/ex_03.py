'''Orçamento com três etapas
Uma pessoa recebe 3.800 durante o mês, ela gasta:
- R$ 1.200 com aluguel;
- R$ 600 com alimentação;
- R$ 300 com transporte;
- R$ 150 com internet;
- R$ 250 com outras despesas.
Do dinheiro que sobrar, ela decide: Guardar 20% e usar o restante para uma viagem. Descubra: 
- Total gasto.
- Valor que sobrou.
- Valor guardado.
- Quanto ficará disponível para a viagem.
'''
salario = 3800
aluguel = 1200
alimentacao = 600
transporte = 300
internet = 150
outras_despesas = 250

total_gastos = aluguel + alimentacao + transporte + internet + outras_despesas
valor_sobrou = salario - total_gastos
valor_guardado = valor_sobrou * 20 / 100
valor_viagem = valor_sobrou - valor_guardado

print(f"Total gasto: {total_gastos:.2f}")
print(f"O valor que sobrou após os gastos foi de: {valor_sobrou:.2f}")
print(f"Valor guardado foi de: {valor_guardado:.2f}")
print(f"Quanto ficou disponível para a viagem? {valor_viagem:.2f}")