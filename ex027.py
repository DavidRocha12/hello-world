#Exercício 27 – Primeiro e último nome de uma pessoa

#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente:

nome = str(input('Digite seu nome completo: ')).strip().upper()
lista = nome.split()
print('Seu nome completo é {}'.format(nome))
print('O seu primeiro nome é {}.'.format(lista[0]))
print('O seu ultimo nome é {}.'.format(lista[-1]))
#se voce utilizar lista[len(lista)-1], faz a mesma coisa.

