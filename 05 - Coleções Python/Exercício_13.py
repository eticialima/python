"""
13) Fazer um programa ler 5 valores e, em seguida, mostrar a posição onde
se encotram o maior e o menor valor.
"""

lista = []

for i in range(5):
    lista.append(float(input("Enter the value: ")))

print(f"\nThe position where the highest value is found: {lista.index(max(lista))}")
print(f"The position where the lowest value is found: {lista.index(min(lista))}")
