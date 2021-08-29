#Exercício 35 – Analisando Triângulo v1.0

#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triângulo.

print('Analisador de triângulos: ')
reta1 = float(input('Digite a 1° reta: '))
reta2 = float(input('Digite a 2° reta: '))
reta3 = float(input('Digite a 3° reta: '))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:#Formula para saber se três retas
#formam um triângulo
    print('Elas podem formar um triângulo!')
else:
    print('Elas não podem formar um triângulo!')
