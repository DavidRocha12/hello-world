#Exercício 4 – Dissecando uma Variável

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possíveis sobre ele:

frase = input('Digite algo: ')
print('O tipo Primitivo é {}.'.format(type(frase)))#Para saber o tipo Primitivo tem que colocar type()
print('É um número? {}'.format(frase.isnumeric()))
print('Está em Maiúscula? {}.'.format(frase.isupper()))
print('Está em Minúscula? {}.'.format(frase.islower()))
print('É um Título? {}.'.format(frase.istitle()))
print('É alfanumérico? {}.'.format(frase.isalnum()))
print('Tem somente espaços? {}.'.format(frase.isspace()))
print('É alfabético? {}.'.format(frase.isalpha()))
