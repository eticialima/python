"""

40) Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""

lista1 = []
cont = 0

for n in range(4):
    lista2 = []

    for j in range(4):
        number = int(input("Enter a number: "))
        lista2.append(number)

        if number > 10:
            cont += 1

    lista1.append(lista2)

print(f"\nThe 4 x 4 matrix has {cont} values greater than 10")
print(lista1)
