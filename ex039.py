#Exercício 39 – Alistamento Militar

#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('Informe o ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - nascimento

print('Sua idade é {}'.format(idade))

if idade == 18:
    print('Vocè está no momento exato para fazer o alistamento no serviço militar!')
elif idade < 18:
    soma = 18 - idade
    futuro = anoatual + soma
    print('Falta {} anos para você se alistar no serviço militar!'
          '\nVocê vai se alistar no ano {}'. format(soma,futuro))
else:
    soma = idade - 18
    passado = anoatual - soma
    print('Já faz {} anos que você se alistou no serviço militar!'
          '\nVocê se alistou no ano de {}.'
          '\nSe Caso não se alistou ainda você está atrasado e pode sofrer penalizações.'
          .format(soma,passado))