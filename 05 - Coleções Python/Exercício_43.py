"""
43) Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e coluna)
do maior valor.
"""

lista1 = []

maior = -9999999999
line = 0
column = 0

for i in range(4):
    lista2 = []

    for j in range(4):
        number = int(input("Enter a number: "))

        if number > maior:
            bigger = number
            line = i
            column = j

        lista2.append(number)

    lista1.append(lista2)

print(f"\n{lista1}")

for i in range(4):

    for j in range(4):
        print(f"{lista1[i][j]}", end='  ')

    print()

print(f"\nThe location of the highest value -> line = {line}; column = {column} ")
