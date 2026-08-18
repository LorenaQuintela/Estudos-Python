'''Uma escola recebeu 96 livros e precisa distribuí-los igualmente entre 8 turmas.
Descubra: Quantos livros cada turma receberá e se haverá livros sobrando.'''

livros = 96
turmas = 8

turma_recebe = livros // turmas
sobra = livros % turmas

print(f"Cada turma receberá: {turma_recebe} livros.")
print(f"Se a turma recebe {turma_recebe} livros e multiplicamos por {turmas} turmas. Temos um total de {livros} livros.")
print(f"Logo os Livros sobrando foi: {sobra}")
