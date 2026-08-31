'''Uma pessoas foi a uma loja e comprou:
- 2 camisetas de R$ 55 cada
- 1 calça de R$ 130
- 1 tênis de R$ 240
A loja oferece 15% de desconto sobre o valor total da compra. Depois aplica o desconto, a pessoa decidiu pagar o valor restante em 3 parcelas iguais.
Descubra: 
Qual valor total antes do desconto? Qual valor do desconto? Qual valor final da compra? E qual valor de cada parcela.'''

camisetas = 55
calca = 130
tenis = 240
desconto = 15

total_sem_desconto = (camisetas * 2) + calca + tenis
valor_do_desconto = total_sem_desconto * desconto / 100
valor_com_desconto = total_sem_desconto - valor_do_desconto
valor_parcela = valor_com_desconto / 3

print(f"Valor total da compra sem desconto foi de R$ {total_sem_desconto:.2f}")
print(f"Valor do desconto R$ {valor_do_desconto:.2f}")
print(f"Valor total da compra depois de aplicar o desconto foi de R$ {valor_com_desconto:.2f}")
print(f"Valor de cada parcela R$ {valor_parcela:.2f}")
