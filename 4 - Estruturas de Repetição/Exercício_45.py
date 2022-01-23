"""
45) Faça um algoritmo que converta uma velocidade expressa em km/h
para m/s e vice versa. Você deve criar um menu com as duas opções de
conversão e com uma opção para finalizar o programa. O usuário poderá
fazer quantas conversões desejar, sendo que o programa só será finalizado quando
a opção de finalizar for escolhida.
"""

while True:
    print("[1] -> Convert express speed to km/h para m/s\n"
          "[2] -> Convert express speed to m/s para km/h \n"
          "[3] -> End the program")
    option = str(input("Enter the number for the option you want: "))

    print()
    if (option == '1') or (option == '[1]'):
        km_h = float(input("Enter the speed expressed in km/h: "))

        print()
        print("Speed in m/s: %.2f\n" % (km_h / 3.6))

    elif (option == '2') or (option == '[2]'):
        m_s = float(input("Enter the speed expressed in m/s: "))

        print()
        print("Speed in km/h: %.2f\n" % (m_s * 3.6))

    elif (option == '3') or (option == '[3]'):
        print('End')
        break

    else:
        print("ERROR!\n")
