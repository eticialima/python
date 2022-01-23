"""
51) Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.
"""

lista1 = []

for i in range(3):
    lista2 = []

    for j in range(3):
        num = int(input("Enter a number: "))
        lista2.append(num)
    lista1.append(lista2)

print()

lista_transposta = []

# Imprimindo a matriz escrita pelo usuário e adicionando os valores na matriz transposta
for i in range(3):
    lista = []

    for j in range(3):
        print(lista1[i][j], end='  ')
        lista.append(lista1[j][i])

    print()
    lista_transposta.append(lista)

print(f"\nList transposed: {lista_transposta}")

for i in range(3):
    for j in range(3):
        print(lista_transposta[i][j], end='  ')
    print()
