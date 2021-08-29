#Exercício 30 – Par ou Ímpar?
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número: '))
int = n % 2 #O resto da divisão por 2 de qualquer número par é 0, e de qualquer número ímpar é 1
print('O seu número é {}'.format(n))
if int == 0:
    print('Esse número é Par.')
else:
    print('Esse numero é Impar.')
