"""
49) Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos
que estão na diagonal principal.
"""

lista1 = []
for i in range(3):

    lista2 = []
    for j in range(3):
        num = int(input("Enter a number: "))
        lista2.append(num)
    lista1.append(lista2)

print()

soma = 0
for i in range(3):
    for j in range(3):
        print(f"{lista1[i][j]}", end='  ')
        if i == j:
            soma += lista1[i][j]

    print()

print(f"\nThe sum of the elements that are on the main diagonal: {soma}")
