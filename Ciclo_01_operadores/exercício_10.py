'''Um produto custa R$240. Ele recebe 15% de desconto e, depois, mais 10% sobre o novo preço. Qual o valor final?
'''
produto = 240
primeiro_desconto = 15
segundo_desconto = 10

valor_do_primeiro_desconto = produto * primeiro_desconto / 100
novo_valor = produto - valor_do_primeiro_desconto

valor_do_segundo_desconto = novo_valor * segundo_desconto / 100
valor_final = novo_valor - valor_do_segundo_desconto

print(f"O valor de 15% de desconto é: R${valor_do_primeiro_desconto:.2f}")
print(f"Então o valor do produto de R$ {produto:.2f} após 15% de desconto é de: R$ {novo_valor:.2f}\n")


print(f"O valor de 10% de desconto é: R$ {valor_do_segundo_desconto:.2f}")
print(f"O novo valor do produto é de R$ {novo_valor:.2f}, após mais 10% de desconto ficou com o valor final de: R$ {valor_final:.2f}")


