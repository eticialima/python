 
nome = 'Geek'  
numeros = [1, 2, 3, 4, 5, 6]  

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


nome = 'Geek'

for letra in nome:
    print(f'{letra}') 
