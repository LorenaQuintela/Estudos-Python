'''Uma pessoa comprou:
- 2 camisetas de R$ 50 cada
- 1 calça de R$ 120
- 1 tênis de R$200
A loja ofereceu 10% de desconto sobre o valor total da compra. Descubra: O valor da compra antes do desconto, o valor do desconto e o valor final pago.'''

camisetas = 50
calca = 120
tenis = 200
desconto = 10

valor_da_compra = (calca + tenis) + camisetas * 2
valor_do_desconto = valor_da_compra * desconto / 100
valor_final_pago = valor_da_compra - valor_do_desconto

print(f"O valor total da compra antes do desconto é de: R$ {valor_da_compra:.2f} reais.")
print(f"O valor do desconto é de: R$ {valor_do_desconto:.2f} reais.")
print(f"O valor final pago após o desconto é de: R$ {valor_final_pago:.2f} reais.")