'''Duas compras e desconto
Uma pessoas foi ao mercado e comprou: 
- 2 pacotes de arroz por R$ 28 cada
- 3 caixas de leite por R$ 7.50 cada
- 2 pacotes de café por R$ 18 cada
Ao chegar ao caixa, recebeu 12% de desconto sobre o valor total. Depois do desconto, pagou a compra e recebeu R$ 50 de troco. Descubra:
- Quanto custou a compra antes do desconto?
- Quanto foi o desconto?
- Quanto ela realmente pagou?
- Quanto dinheiro ela entregou ao caixa?
'''
arroz = 28 * 2
leite = 7.50 * 3
cafe = 18 * 2

valor_total = arroz + leite + cafe
valor_desconto = valor_total * 12 / 100
valor_pago = valor_total - valor_desconto
valor_entregue = valor_pago + 50


print(f"Quanto custou a compra antes do desconto? {valor_total:.2f}")
print(f"Quanto foi o valor do desconto? {valor_desconto:.2f}")
print(f"Quanto ela realmente pagou? {valor_pago:.2f}")
print(f"Quanto dinheiro ela entregou ao caixa? {valor_entregue:.2f}")