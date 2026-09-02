'''Pontuação -> Em um jogo, uma pessoa terminou uma partida com 750 pontos.
Outra pessoa terminou com 820 pontos. Descubra:

1- A primeira pessoa fez mais pontos que a segunda? False
2- A segunda pessoa fez mais pontos que a primeira? True
3- As duas fizeram a mesma pontuação? False
4- A diferença entre as pontuações é maior que 50  pontos? True '''

pessoa_1 = 750
pessoa_2 = 820

diferenca = pessoa_2 - pessoa_1

print(f"A primeira pessoa fez mais pontos que a segunda? {pessoa_1 > pessoa_2}")
print(f"A segunda pessoa fez mais pontos que a primeira? {pessoa_2 > pessoa_1}")
print(f"As duas fizeram a mesma pontuação? {pessoa_1 == pessoa_2}")
print(f"A diferença entre as pontuações é maior que 50  pontos? {diferenca > 50}")