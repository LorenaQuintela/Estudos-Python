'''Uma pessoa recebe R$ 2.500 por mês. Seus gastos são: - aluguel: R$ 900
- alimentação: R$ 450
- transporte: R$ 250
- internet R$ 100
- lazer R$ 200
Depois  de pagar tudo, ela decide guardar 30% do dinheiro que sobrou. Descubra: 
- Quanto foi o gasto no total ?
- Quanto sobrou depois dos gastos?
- Quanto continuará disponivel depois de guardar esse dinheiro? '''

salario = 2500
aluguel = 900
alimentacao = 450
transporte = 250
internet = 100
lazer = 200

# valor total gasto é de 1.900 reais
gastos = aluguel + alimentacao + transporte + internet + lazer 
# 1900 - 2500
valor_sobrou = salario - gastos

guardar = valor_sobrou * 30 / 100
valor_disponivel = valor_sobrou - guardar

print(f"Quanto foi o gasto no total? R$ {gastos:.2f}.")
print(f"Quanto sobrou depois dos gastos? R$ {valor_sobrou:.2f}.")
print(f"Quanto continuará disponivel depois de guardar esse dinheiro? R$ {valor_disponivel:.2f}.")
