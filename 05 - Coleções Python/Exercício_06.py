"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.
"""

lista = []

for i in range(10):
    lista.append(int(input("Enter the value: ")))

print(f"\nThe greatest element of the vector is: {max(lista)}")
print(f"The smallest element of the vector is: {min(lista)}")
