# Define uma lista de livros
livros = [
    "A Guerra dos Tronos",
    "Harry Potter e a Pedra Filosofal",
    "O Senhor dos Anéis - A Sociedade do Anel",
    42,
    3.14
]

# Verifica o tipo de cada item na lista de livros usando type()
for livro in livros:
    print("Tipo de objeto:", type(livro))


## Como criar um objecto (class) usando a função type()

# Defini uma classe "Pessoa" usando type()
Pessoa = type("Pessoa", (object,), {"nome": "", "idade": 0})

# Instancia um objeto da classe "Pessoa"
pessoa = Pessoa()
pessoa.nome = "João"
pessoa.idade = 30

# Verifica o tipo do objeto "pessoa"
print("Tipo de objeto:", type(pessoa))

# Imprime as informações da pessoa
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)

