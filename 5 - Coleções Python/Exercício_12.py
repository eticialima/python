"""
12) Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores
lidos juntamente com o maior, o menor e a média dos valores.
"""

lista = []

for i in range(5):
    lista.append(float(input("Enter a decimal number: ")))

print(f"\nThe values read: ", end='')
print(* lista, sep=', ')

print(f"The largest number of values read: {max(lista)}")
print(f"The smallest number of values read: {min(lista)}")
print(f"The average of the values read: {sum(lista) / len(lista)}")
