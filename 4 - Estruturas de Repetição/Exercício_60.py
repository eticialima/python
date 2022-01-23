"""
60) Faça um programa que leia vários números, calcule e mostre:
(a) A soma dos números digitados
(b) A quantidade de números digitados
(c) A média dos números digitados
(d) O maior número digitado
(e) O menor número digitado
(f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
"""

soma = 0
cont = 0
maior = 0
menor = 0

soma_pares = 0
cont_pares = 0

while True:

    numero = int(input("Enter the value: "))

    if numero != 0:
        soma += numero

        if cont == 0:
            menor = numero
            maior = numero

        if numero % 2 == 0:
            soma_pares += numero
            cont_pares += 1

        if menor > numero:
            menor = numero

        elif maior < numero:
            maior = numero

        cont += 1

    else:
        break

if cont_pares == 0:
    cont_pares = 1

print()
print(f"The sum of the numbers entered: {soma}")
print(f"The number of numbers entered: {cont}")
print("The average of the numbers entered: %.2f" % (soma / cont))
print(f"The highest number entered: {maior}")
print(f"The smallest number entered: {menor}")
print(f"The average of the even numbers: %.2f" % (soma_pares / cont_pares))
