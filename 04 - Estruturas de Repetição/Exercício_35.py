"""
35) Faça um programa que some os números impares contidos em um intervalo
definido pelo usuário. O usuário define o valor inicial do intervalo
e o valor final deste intervalo e o programa deve somar todos os números
impares contidos. Caso o usuário digite um intervalo inválido (começando por um valor
maior que o valor final) deve ser escrito uma mensagem de erro na tela, "Intervalo de
valores inválido" e o programa termina. Exemplo de tela de saída:
Digte o valor incial e valor final: 5
10
Soma dos ímpares neste intervalo: 21
"""

valor_inicial = int(input("Enter the starting value of the range: "))
valor_final = int(input("Enter the final value of the range: "))

print()
if valor_inicial < valor_final:
    soma = 0

    for i in range(valor_inicial, valor_final+1):
        if i % 2 == 1:
            soma += i

    print(f"Sum of odd numbers in this range: {soma}")

else:
    print("Invalid range of values")
