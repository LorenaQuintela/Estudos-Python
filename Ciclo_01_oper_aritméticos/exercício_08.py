'''Uma blusa custa R$ 180.00 reais.
- Primeiro ela recebe um desconto de 10%.
- Depois sobre o novo preço, é aplicado 5% de desconto.- - Qual o preço final da blusa? '''

blusa = 180

primeiro_desconto = blusa * 10 / 100
primeiro_valor = blusa - primeiro_desconto

segundo_desconto = primeiro_valor * 5 / 100
valor_final = primeiro_valor - segundo_desconto

print(f"Primeiro preço após 10% de desconto foi de: R$ {primeiro_valor:.2f}")
print(f"O preço final da blusa sobre o novo preço foi de: R$ {valor_final:.2f}")