"""
47) Faça um programa que apresente um menu de opções para o cálculo
das seguintes operações entre dois números:
    - adição (opção 1)
    - subtração (opção 2)
    - multiplicação (opção 3)
    - divisão (opção 4)
    - saídaa (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejaada,
a exibição do resultado e a volta ao menu de opções. O programa só termina
quando for escolhida a opção de saída (opção 5).
"""

while True:
    print("* addition (opção 1)\n"
          "* subtraction (opção 2)\n"
          "* multiplication (opção 3)\n"
          "* division (opção 4)\n"
          "* exit (opção 5)")
    option = int(input("Enter the number for the desired option: "))

    print()
    if (option >= 1) and (option <= 4):

        number_01 = int(input("Enter the value: "))
        number_02 = int(input("Enter the value: "))

        if option == 1:
            print(f"{number_01} + {number_02} = {number_01 + number_02}\n")

        elif option == 2:
            print(f"{number_01} - {number_02} = {number_01 - number_02}\n")

        elif option == 3:
            print(f"{number_01} * {number_02} = {number_01 * number_02}\n")

        elif option == 4:
            print(f"{number_01} / {number_02} = {number_01 / number_02}\n")

    elif option == 5:
        print("END!")
        break

    else:
        print("ERROR!")
