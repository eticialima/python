def dobro(num):
    return num * 2

lista = [1, 2, 3, 4, 5]
resultado = list(map(dobro, lista))

print(resultado)
# Output: [2, 4, 6, 8, 10]
