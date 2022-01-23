"""
33) Dados n e dois números inteiros positivos, i e j, diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos
de i ou de j e ou de ambos. Exemplo: Para n = 6, i = 2 e j = 3 a saída
deverá ser: 0,2,3,4,6,8.
"""
number = int(input("Enter the value of n: "))

print()

if number > 0:
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))

    print()
    if value1 > 0 and value2 > 0:
        lista = []

        print(f"The first natural n which are multiples of {value1} or {value2} and or both:")

        for i in range(number):
            if not (value1 * i in lista):
                lista.append(value1 * i)

            if not (value2 * i in lista):
                lista.append(value2 * i)

        lista.sort()

        for i in range(number):
            print(lista[i])

    else:
        print("Numbers cannot be zero or negative")

else:
    print("The value of n cannot be zero or negative")
