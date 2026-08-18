'''Uma pessoa foi as compras e comprou:
- 3 camisetas por R$ 45 cada.
- 2 calças por R$ 80 cada.
- 1 tênis por R$ 150.
Descubra quanto essa pessoa gastou no total.'''
camisetas = 45 * 3 # Quantidade = 3
calcas = 80 * 2 # Quantidade = 2
tenis = 150

#valor_camisetas = camisetas * 3
#valor_calcas = calcas * 2
#valor_total = valor_camisetas + valor_calcas + tenis

valor_total = camisetas + calcas + tenis

print(f"O valor total gasto por essa pessoa foi de: R$ {valor_total:.2f} reais.")
