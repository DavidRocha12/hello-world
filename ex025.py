#Exercício 25 – Procurando uma string dentro de outra

#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome:

nome = str(input('Digite seu nome em extensso: ')).strip().upper()
print('O seu nome é {}, e é {} que tem "SILVA" em seu nome.'.format(nome, 'SILVA' in nome))
