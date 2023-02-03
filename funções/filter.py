def é_par(num):
    return num % 2 == 0

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(filter(é_par, lista))

print(resultado)
# Output: [2, 4, 6, 8, 10]



## Neste exemplo, a função tem_letra_a é criada para verificar se uma palavra contém a letra "a".
# Em seguida, a função filter é usada para filtrar apenas as palavras da lista palavras que contêm
# a letra "a", e o resultado é convertido em uma lista.
def tem_letra_a(palavra):
    return 'a' in palavra

palavras = ['casa', 'carro', 'pessoa', 'amigo']
resultado = list(filter(tem_letra_a, palavras))

print(resultado)
# Output: ['casa', 'carro', 'amigo']


# filtrar palavras com a primeira letra específica.
def começa_com_a(palavra):
    return palavra[0] == 'a'

palavras = ['casa', 'carro', 'pessoa', 'amigo']
resultado = list(filter(começa_com_a, palavras))

print(resultado)
# Output: ['amigo']

