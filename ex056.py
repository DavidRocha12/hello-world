#Exercício 56 – Analisador completo

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from datetime import date
maisvelho = 0
homemvelho = ''
soma = 0
contador = 0
for pessoa in range(1, 5):
    nome = str(input('Qual é o nome da {}° pessoa: '.format(pessoa))).strip().upper()
    nascimento = int(input('Qual é o ano de nascimento: '))
    ano = date.today().year
    idade = ano - nascimento
    sexo = str(input('Qual é o sexo F/M: ')).strip().upper()
    print('O nome da pessoa é {}, a idade é {} anos e ela é do sexo {}'.format(nome, idade, sexo))
    soma += idade
    media = soma / 4
    if sexo == 'M':
        if pessoa == 1:
            maisvelho = idade
            homemvelho = nome
        elif idade > maisvelho:
                maisvelho = idade
                homemvelho = nome
    elif sexo == 'F':
        if idade < 20:
            contador += 1
print('A média de idade do grupo é {} anos.'.format(media))
print('O Nome do homem mais velho é {}, a idade dele é {} anos.'.format(homemvelho, maisvelho))
print('No grupo existe {} mulher(es) menor de 20 anos.'.format(contador))
