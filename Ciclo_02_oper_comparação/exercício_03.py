'''Situação Real
Uma loja definiu que compras acima de R$ 200 recebem uma condição especial.
Uma cliente fez uma compra de R$ 250.
1- A compra é maior que R$ 200? True
2- A compra é menor que R$ 200? False
3- A compra é exatamente R$ 200? False
4- A compra é maior ou igual R$ 200? True '''

loja_definiu = 200
cliente_comprou = 250

print("A compra é maior que R$ 200?",cliente_comprou > loja_definiu )
print("A compra é menor que R$ 200?", cliente_comprou < loja_definiu)
print("A compra é exatamente R$ 200?", loja_definiu == cliente_comprou)
print("A compra é maior ou igual R$ 200? ", cliente_comprou >= loja_definiu )