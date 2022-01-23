"""
11) Faça um programa que preencha um vetor com 10 números reais,
calcule e mostre a quantidade de números negativos e a soma dos números
positivos desse vetor.
"""

lista = []
counter = []
adder = []

for i in range(10):
    lista.append(float(input(f"Enter a decimal number: ")))

    if lista[i] < 0:
        counter.append(lista[i])

    else:
        adder.append(lista[i])

print(f"\nThe number of negative numbers: {len(counter)}")
print(f"The sum of the positive numbers: {sum(adder)}")
