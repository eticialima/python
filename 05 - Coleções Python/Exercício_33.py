"""
33) Faça um programa que leia um vetor de 15 posições e o compacte, ou
seja, elimine as posições com valor zero. Para isso, todos os elementos
à frente do valor zero, devem ser movidos uma posição para trás no vetor.
"""

vector = []

for i in range(15):
    vector.append(int(input("Enter the value: ")))

vector2 = []

print()
for i in vector:

    if i != 0:
        vector2.append(i)

print(vector2)
