"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""

lista = []

for i in range(8):
    lista.append(int(input("Enter the value: ")))

x = int(input("\nEnter a value for the position of the vector: "))
y = int(input("Enter another value referring to the position of the vector: "))

print(f"\nSum of the values found in the respective positions: {lista[x] + lista[y]}")
