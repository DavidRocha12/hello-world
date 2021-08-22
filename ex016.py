#Exercício 16 – Quebrando um número

#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção Inteira.
from math import trunc
n = float(input('Digite um número: '))
print('A porçãp inteira do Numero {} é {}.'.format(n, trunc(n)))