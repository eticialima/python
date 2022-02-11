"""
61) Faça um programa que leia duas matrizes A e B
de tamanho 3 x 3 e calcule C = A * B.
"""

matriz_a = []
matriz_b = []

for i in range(3):
    matriz = []

    for j in range(3):
        num = int(input("Enter a number for the first matrix: "))
        matriz.append(num)
    matriz_a.append(matriz)

print()
for i in range(3):
    matriz = []

    for j in range(3):
        num = int(input("Enter a number for the second matrix: "))
        matriz.append(num)
    matriz_b.append(matriz)

print()

matriz_c = []
for i in range(3):
    matriz = []

    for j in range(3):
        matriz.append(matriz_a[i][j] * matriz_b[i][j])
    matriz_c.append(matriz)

for i in range(3):
    for j in range(3):
        print(matriz_c[i][j], end='  ')
    print()
