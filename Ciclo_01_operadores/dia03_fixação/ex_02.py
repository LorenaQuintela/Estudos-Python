'''Uma pequena fábrica produziu  347 peças.
As peças serão colocadas em caixas com capacidade para 12 peças. Descubra: 
- Quantas caixas podem ser preenchidas completamente? 
- Quantas peças sobram?
Depois, a fábrica decidiu separar as peças que conseguiram ser colocadas nas caixas completas igualmente entre 5 setores.
- Quantas peças cada setor receberá?
- Quantas peças ficarão sem ser distribuídas entre os setores? '''

pecas = 347
caixas = 12
setores = 5

caixas_preenchidas_compl = pecas // caixas
pecas_restante = pecas % caixas

quantidade_de_pecas = pecas - pecas_restante

peca_por_setor = quantidade_de_pecas // setores
pecas_restante_setor = quantidade_de_pecas % setores


print(f"Quantas caixas foram preenchidas completamente? {caixas_preenchidas_compl}")
print(f"Quantas peças sobraram? {pecas_restante}")

print(f"Quantas peças cada setor recebeu? {peca_por_setor}")
print(f"Quantas peças ficarão sem ser distribuídas entre os setores? {pecas_restante_setor}")
