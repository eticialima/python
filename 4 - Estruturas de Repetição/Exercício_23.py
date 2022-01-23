"""
23) Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

number = int(input("Enter the number: "))

print()
if number > 0:
        print("Os divisores desse número são: ")
        for n in range(1, number + 1):
                if number % n == 0:
                        print(n)

else:
        print("The number must be positive!")
