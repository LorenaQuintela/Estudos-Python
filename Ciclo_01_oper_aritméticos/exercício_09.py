'''Uma loja possui 83 produtos e quer organizar 10 produtos em cada caixa. Quantas caixas completas serão formadas e quantos produtos ficarão de fora?
'''
produtos = 83
caixa = 10

resultado_caixas_completas = produtos // caixa
produtos_de_fora = produtos % caixa

print(f"Consegui {resultado_caixas_completas} caixas completas de produtos.")
print(f"E {produtos_de_fora} produtos ficarão fora da caixa.")