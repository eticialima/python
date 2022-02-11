"""
7) Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""

lista = []

for i in range(10):
    lista.append(int(input("Enter the value: ")))

print(f"\nVetor: {lista}")
print(f"Largest element: {max(lista)}")
print(f"Position in which the largest element is found: {lista.index(max(lista))}")
