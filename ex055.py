#Exercício 55 – Maior e menor da sequência

#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0
for pessoa in range(1, 6):
    peso = float(input('Qual é o peso da {}° pessoa: '.format(pessoa)))
    print('O peso da pessoa é {}kg.'.format(peso))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('A pessoa com maior peso tem {}kg.'.format(maior))
print('A pessoa com menor peso tem {}kg.'.format(menor))