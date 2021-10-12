#Exercício 41 – Classificando Atletas

#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

print('-' * 20, 'Categoria de Atletas', '-' * 20)
print('')

from datetime import date#biblioteca para colocar data ou saber a data atual.
atleta = int(input('Digite o ano de nascimento do Atleta: '))

ano = date.today().year#variavel para saber o ano atual
idade = ano - atleta#variavel para calcular e saber a idade do atleta

print('')
if idade <= 9:#condição aninhaa para saber a categoria do atleta.
    categoria = 'MIRIM'#Váriavel para fazer a troca das categorias.
elif idade == 10 or idade <= 14:
    categoria = 'INFANTIL'
elif idade == 15 or idade <= 19:
    categoria = 'JUNIOR'
elif idade == 20 or idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print('O Atleta tem {} anos de idade.'.format(idade))
print('E está na categoria {} !!!'.format(categoria))
print('')
print('-' * 64)