'''Ex05: Um produto custa R$ 250 reais, e ele está com desconto de 10%. Calcule:
Quanto é o desconto? 
Qual será o preço final?'''

produto = 250
porcentagem = 10

preco_do_desconto = (porcentagem / 100) * produto
preco_final = produto - preco_do_desconto

# Para não esquecer :.2f força a exibição de duas casas decimais para ficar com cara de reais.
print(f"O valor do desconto é de R$ {preco_do_desconto:.2f} reais.")
print(f"Preço final é de R$ {preco_final:.2f} reais.")
