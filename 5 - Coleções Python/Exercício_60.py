"""
60) Faça um programa que leia duas matrizes 2 x 2 com valores reais.
Ofereça ao usuário um menu de opções:
(a) somar as duas matrizes
(b) subtrair a primeira matriz da segunda
(c) adicionar uma constante às duas matrizes
(d) imprimir as matrizes
"""

matriz1 = []

# A primeira matriz 2 x 2
for i in range(2):
    matriz2 = []

    for j in range(2):
        num = int(input("Enter a number for the first matrix: "))
        matriz2.append(num)
    matriz1.append(matriz2)

print()

matriz2 = []

# A segunda matriz 2 x 2
for i in range(2):
    matriz3 = []

    for j in range(2):
        num = int(input("Enter a number for the second matrix: "))
        matriz3.append(num)
    matriz2.append(matriz3)

while True:
    opcao = str(input("\nOptions menu:\n\n"
                      "(a) add the two matrices\n"
                      "(b) subtract the first matrix from the second\n"
                      "(c) add a constant to the two matrices\n"
                      "(d) print the matrices\n\n"
                      "Enter only the letter for the option you want: "))

    print()

    if opcao.lower() == 'a':
        soma_matrizes = []
        print("The sum of the elements of the same position of the matrix: ")

        for i in range(2):
            soma = []
            for j in range(2):
                soma.append(matriz1[i][j] + matriz2[i][j])
            soma_matrizes.append(soma)

        for i in range(2):
            for j in range(2):
                print(soma_matrizes[i][j], end='  ')
            print()

    elif opcao.lower() == 'b':
        subtrair_matrizes = []

        print("Subtracting the elements from the same position in the matrix:")

        for i in range(2):
            subtrair = []

            for j in range(2):
                subtrair.append(matriz1[i][j] - matriz2[i][j])
            subtrair_matrizes.append(subtrair)

        for i in range(2):
            for j in range(2):
                print(subtrair_matrizes[i][j], end='  ')

            print()

    elif opcao.lower() == 'c':
        constante = int(input("Type an integer constant: "))

        for i in range(2):
            for j in range(2):
                matriz1[i][j] += constante
                matriz2[i][j] += constante

    elif opcao.lower() == 'd':

        print("Headquarters 1:")
        for i in range(2):

            for j in range(2):
                print(matriz1[i][j], end='  ')

            print()

        print("\nHeadquarters 2:")
        for i in range(2):
            for j in range(2):
                print(matriz2[i][j], end='  ')

            print()

    else:
        print("CLOSED!")
        break
