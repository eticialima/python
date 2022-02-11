"""
30)Faça um programa que leia dois vetores de 10 elementos. Crie
um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que
contém apenas os números que estão em ambos os vetores. Não deve
conter números repetidos.
"""

vector_1 = []
vector_2 = []

for n in range(10):
    vector_1.append(int(input("Type an element from the first vector: ")))

print()
for n in range(10):
    vector_2.append(int(input("Type an element from the second vector: ")))

set_1 = set(vector_1)
set_2 = set(vector_2)

interseccao = set_1.intersection(set_2)

print(f"\nThe numbers that are in both vectors: {interseccao}")
