"""
29) Faça um programa que receba 6 números inteiros e mostre:
    . Os números pares digitados;
    . A soma dos números pares digitados;
    . Os números ímpares digitados;
    . A quantidade de número ímpares digitados;
"""

lista = []

for i in range(6):
    lista.append(int(input("Enter the value: ")))

even = []
odd = []

for i in lista:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"\nThe even numbers entered: {even}")
print(f"The sum of the even numbers entered: {sum(even)}")
print(f"The odd numbers entered: {odd}")
print(f"Anumber of odd numbers entered: {len(odd)}")
