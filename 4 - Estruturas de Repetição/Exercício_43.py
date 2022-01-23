"""
43) Faça um programa que leia um número inderterminado de idades de
indivíduos (pare quando for informada a idade 0), e calcule a idade
média desse grupo.
"""

age = int(input("Enter an age: "))

if age != 0:
    media = age
    cont = 1

    while True:
        age = int(input("Enter an age: "))

        if age != 0:
            media += age
            cont += 1

        else:
            break

    print()
    print("Mean age of the group: %.2f " % (media / cont))

else:
    print()
    print("Age cannot be zero!")
