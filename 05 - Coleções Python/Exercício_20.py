"""
20) Escreva um programa que leia números inteiros no intervalo [0,50]
e os armazene em um vetor com 10 posições. Preencha um segundo vetor
apenas com os números ímpares do primeiro vetor. Imprima os dois vetores,
2 elementos por linha.
"""

lista = []
odd = []

for n in range(10):
    number = int(input("Enter a number in the range [0,50]: "))

    if (number >= 0) and (number <= 50):
        lista.append(number)

        if number % 2 == 1:
            odd.append(number)

print(f"\nFirst vector: ")

for n in range(0, len(lista), 2):
    print(f"{lista[n]}   ", end='')

    if len(lista) > n + 1:
        print(lista[n + 1])

print(f"\nSecond vector: ")

for n in range(0, len(odd), 2):
    print(f"{odd[n]}", end='')

    if len(odd) > n + 1:
        print(odd[n + 1])
