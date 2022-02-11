"""
39) Faça um programa que calcule a área de um triângulo, cuja base e altura
são fornecida pelo usuário. Esse programa não pode permitir a entrada de dados inválidos,
ou seja, medidas menores ou iguais a 0.
"""

base = int(input("Enter the size of the base of the triangle: "))

if base > 0:
    altura = int(input("Enter the size of the height of the triangle: "))
    print()

    if altura > 0:
        area_triangulo = (base * altura) / 2
        print(f"The triangle area is {area_triangulo}")

    else:
        print("Invalid height!")

else:
    print()
    print("Invalid base!")
