""" 
Problema: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. 
"""
nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

print('Média: {:.1f}'.format(media))
