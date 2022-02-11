"""
19) Escreva um algoritmo que leia um número inteiro entre 100 e 999
e imprima na saída cada um dos algarismos que compõem o número.
"""

number = int(input('Enter a number between 100 and 999: '))
print()

if (number >= 100) and (number <= 999):
        lista = str(number)

        print('Each digit making up the number: ')

        for x, y in enumerate(lista):
                print(y)
else:
        print('The number must be between 100 and 900')
