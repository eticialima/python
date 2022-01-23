"""
15) Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
eliminando elementos repetidos.
"""

lista = []

for i in range(20):
    lista.append(int(input("Enter the value: ")))

conjunto = set(lista)

print("\nThe distinct elements of the vector: ", end='')
print(* conjunto, sep=', ')
