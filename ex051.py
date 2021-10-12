#Exercício 51 – Progressão Aritmética

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Qual é o Primeiro termo: '))
razao = int(input('Qual é a razão da PA(Progressão Aritmética): '))
print('')
for pa in range(1,11):
    soma = termo + (pa - 1) * razao
    print('O {}° termo da PA é {}'.format(pa, soma))

#Este exercício o professor não colocou a formula dentro do for,
# e no lugar do pa na formula o professor coloca 10