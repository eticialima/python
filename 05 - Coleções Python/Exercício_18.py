"""
18) Faça um programa que leia um vetor de 10 números. Leia um
número x. Conte os múltiplos de um número inteiro x num vetor
e mostre-os na tela.
"""

lista = []

for i in range(10):
    lista.append(int(input("Enter the value: ")))

x = int(input("\nEnter the value x: "))

multiplo = []

for i in range(10):
    multiplo.append(x * lista[i])

print(f"\nMultiples of {x} according to the values entered: ")
print(*multiplo, sep=', ')
