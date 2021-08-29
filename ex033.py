#Exercício 33 – Maior e menor valores

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))

#Você pode retirar um if já considerando o n1 menor e começando o if apartir do n2 o mesmo acontece para o maior.
