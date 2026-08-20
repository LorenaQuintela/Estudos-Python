'''
Uma escola recebeu 157 cadernos. Eles serão colocados em caixas com 12 cadernos em cada caixa. Descubra: 
- Quantas caixas completas podem ser montadas? 
- Quantos cadernos ficarão sobrando?

Depois imagine que esses cardenos sejam distribuídos igualmente entre 5 salas, usando apenas cadernos que conseguiram ser colocados nas caixas completas.
- Quantos cadernos cada sala receberá?
- Quantos cadernos ficarão sem ser distruídos? '''
cadernos = 157
caixas = 12

caixas_completas = cadernos // caixas
cadernos_sobrando = cadernos % caixas
print(f"Quantas caixas completas podem ser montadas? {caixas_completas} com 12 cadernos.")
print(f"Quantos cadernos ficarão sem ser distruídos?  {cadernos_sobrando} caderno.\n")


print('''Depois imagine que esses cardenos sejam distribuídos igualmente entre 5 salas, usando apenas cadernos que conseguiram ser colocados nas caixas completas.\n''')
cadernos_caixas_completas = 156
salas = 5

sala_recebe = cadernos_caixas_completas // salas
caderno_sem_distruição = cadernos_caixas_completas % salas

print(f"Quantos cadernos cada sala receberá? {sala_recebe}.")
print(f"Quantos cadernos ficarão sem ser distruídos? {caderno_sem_distruição}.")