# Recebe a distância percorrida por um carro
distancia = int(input("Informe a distância percorrida pelo carro: "))

# Recebe a velocidade média do carro
velocidade_media = int(input("Informe a velocidade média do carro: "))

# Calcula o tempo de viagem
tempo = distancia / velocidade_media

# Usa a função abs para garantir que o resultado seja sempre positivo
tempo = abs(tempo)

# Imprime o resultado
print("O tempo de viagem é de aproximadamente", tempo, "horas")

## abs(-10)
## retorna 10
