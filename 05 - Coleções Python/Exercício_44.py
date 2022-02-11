"""
44) Leia uma matriz 5 x 5. Leia também um valor X. O programa
deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização
(linha e coluna) ou mensagem de "não encontrado".
"""

lista1 = []

for i in range(5):
    lista2 = []

    for j in range(5):
        num = int(input("Enter a number: "))
        lista2.append(num)

    lista1.append(lista2)

x = int(input("\nEnter a number x: "))

print(f'\n{lista1}')

cont = 0
for i in range(5):

    for j in range(5):
        if x == lista1[i][j]:
            cont += 1
            print(f"\nThe value {x} is found in line {i} and in the column {j}")

if cont == 0:
    print("\nNot found")
