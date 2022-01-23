"""
8) Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre
na tela os valores lidos na ordem inversa
"""

lista = []

for i in range(6):
    lista.append(int(input("Enter the value: ")))

print("\nValues in reverse order: ", end='')
print(* lista[::-1], sep=', ')
