'''Organização de estoque
Uma loja recebeu 524 produtos. Primeiro, os produtos serão organizados em caixas contendo 15 produtos cada.Depois, somente os produtos que estiverem dentro das caixas completas serão distribuídos igualmente entre 7 prateleiras. Descubra: 
- Quantas caixas completas serão formadas?
- Quantos produtos ficarão fora das caixas?
- Quantos produtos irão para cada prateleira?
- Quantos produtos ficarão sem espaço nas prateleiras?
'''
produtos = 524
caixas = 15

caixas_completas = produtos // caixas
produtos_fora = produtos % caixas
qtd_das_caixas_completas = produtos - produtos_fora

prateleiras = 7
qtd_prateleira_completa = qtd_das_caixas_completas // prateleiras
qtd_sobra_prateleira = qtd_das_caixas_completas % prateleiras


print(f"Quantas caixas completas serão formadas? {caixas_completas}")
print(f"Quantos produtos ficarão fora das caixas? {produtos_fora}")
print(f"Quantos produtos irão para cada prateleira? {qtd_prateleira_completa}")
print(f"Quantos produtos ficarão sem espaço nas prateleiras? {qtd_sobra_prateleira}")
#print(valor_das_caixas_completas)