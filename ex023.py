#Exercício 23 – Separando dígitos de um número:

#Faça um programa que leia um número de 0 a 9999
#e mostre na tela cada um dos dígitos separados.

n = int(input('Informe um número: '))
print('Analisando o Número: {}.'.format(n))
n1 = n // 1 % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10
print('A unidade é {}'.format(n1))
print('A dezena é {}.'.format(n2))
print('A centena é {}.'.format(n3))
print('O milhar é {}.'.format(n4))