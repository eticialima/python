"""
26) Faça um algoritmo que encontre o primeiro múltiplo de 11, 13
ou 17 após um número dado.
"""

number = int(input("Enter the number: "))

lista = [11, 13, 17]

print()
print(f"First multiple of 11, 13 or 17 of {number}:")
for x, y in enumerate(lista):
        print(number * y)
