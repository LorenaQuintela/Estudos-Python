'''Uma pessoa possui R$ 1000 reais.
Durante o mês, ela teve os seguintes gastos:
- Aluguel: R$ 450
- Mercado: R$ 230
- Transporte: R$ 120
- Lazer: R$ 75 
Descubra quanto dinheiro restou.'''
saldo = 1000
aluguel = 450
mercado = 230
transporte = 120
lazer = 75

valor_resto = saldo - (aluguel + mercado + transporte + lazer)

print(f"O dinheiro que restou foi de: R$ {valor_resto:.2f} reais.")