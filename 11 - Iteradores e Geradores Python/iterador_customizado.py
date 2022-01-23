 
# Criando um Iterador Customizado


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


# Usando o Iterador Criado
for n in Contador(1, 61):
    print(n)
 
