"""
16) Faça um programa que leia um vetor de 5 posições para números reais e,
depois, um código inteiro, Se o código for zero, finalize o programa;
se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem
inversa. Caso, o código for diferente de 1 e 2 escreva uma mensagem informando
que o código é inválido
"""

lista = []

for i in range(5):
    lista.append(float(input("Enter a decimal number: ")))

while True:
    codigo = int(input("\nThe code number: "))

    if codigo == 0:
        break

    elif codigo == 1:
        print(f"Vector in direct order: {lista}")

    elif codigo == 2:
        print(f"Vector in reverse order: {lista[::-1]}")

    else:
        print("Invalid code")
