""" 
Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. 
"""
nome = input('Nome: ').strip()
print('Tem "SILVA" no seu nome: ', 'SILVA' in nome.upper())