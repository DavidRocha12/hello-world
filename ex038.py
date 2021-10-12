#Exercício 38 – Comparando números
#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1 = int(input('Digite o 1° Número: '))
n2 = int(input('Digite o 2° Número: '))

print('Os números que você digitou é \033[31m{}\033[m e \033[31m{}\033[m.'.format(n1, n2))

if n1 > n2:
    print('\033[32mO Primeiro valor é maior!\033[m')
elif n2 > n1:
    print('\033[34mO segundo valor é maior!\033[m')
elif n1 == n2:
    print('\033[33mNão existe valor maior, os dois são iguais!\033[m')