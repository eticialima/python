"""
9) Crie um programa que lê 6 valores inteiros pares e,
em seguida, mostre na tela os valores lidos na ordem inversa.
"""

lista = []

for i in range(6):
    par = int(input("Enter an even value: "))
    if par % 2 == 0:
        lista.append(par)

    else:
        print("Enter even numbers only.\n")

print("\nEven values in reverse order: ", end='')
print(* lista[::-1], sep=', ')
