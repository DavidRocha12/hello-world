#Exercício 54 – Grupo da Maioridade

#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for pessoas in range (1, 8):
    nascimento = int(input('Digite o ano {}° ano de nascimento: '.format(pessoas)))
    ano = date.today().year
    idade = ano - nascimento
    print('Essa pessoa tem {} ano(s) de idade.'.format(idade))
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('Nesse grupo tem {} pessoas que já atingiram a maior idade.'.format(maior))
print('Nesse grupo tem {} pessoas que não atingiram a maior idade.'.format(menor))
