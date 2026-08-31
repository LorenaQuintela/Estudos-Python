''' Produto custa R$ 300.00. Ele está com 20% de desconto. Quanto vale o desconto? Qual é o preço final?'''

produto = 300
desconto = 20

valor_desconto = 300 * 20 / 100
valor_final = produto - valor_desconto

print(f"O valor do desconto é de: R$ {valor_desconto:.2f}")
print(f"O valor do preço final: R$ {valor_final:.2f}")