#Exercício 32 – Ano Bissexto

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date#Bibliote e função para saber a data

print('Veja qual ano é Bissexto e qual não é !')
data = int(input('Digite um ano qualquer, se quiser mostrar o ano atual digite 0: '))

if data == 0:
    data = date.today().year#função para saber a data atual

print('O ano que você digitou é {}.'.format(data))

if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:#formula para saber se o ano é bissexto
    print('O ano é Bissexto')
else:
    print('Este ano não é Bissexto !')
