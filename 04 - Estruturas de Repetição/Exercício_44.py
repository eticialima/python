"""
44) Leia um número positivo do usuário, então, calcule e imprima a
sequência Fibonacci até o primeiro número superior lido. Exemplo:
se o usuário informou o número 30, asequência a ser impressa será
0 1 1 2 3 5 8 13 21 34.
"""

number = int(input("Enter the number: "))
soma1 = 0
soma2 = 1
print()
if number > 0:
    print('0')
    print('1')

    print(f"Sequência Fibonacci até o primeiro número superior lido: ")

    for i in range(0, number):
        soma1 += soma2
        soma2 += soma1

        print(soma1)

        if soma1 > number:
            break

        print(soma2)

        if soma2 > number:
            break

else:
    print("Invalid Number")
