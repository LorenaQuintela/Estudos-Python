'''Ex04: Uma empresa possui 57 funcionários. Ela quer formar grupos de 8 pessoas. Descubra quantos grupos completos podem ser formados? E quantas pessoas ficarão de fora.'''

funcionarios = 57
pessoas = 8

resultado_grupo = funcionarios // pessoas
print(f"Foram formados {resultado_grupo} grupos completos de 8 pessoas.")
resultado_sobra = funcionarios % pessoas
print(f"E {resultado_sobra} pessoa ficou de fora.")