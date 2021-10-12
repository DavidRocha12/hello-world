#Exercício 59 – Criando um Menu de Opções

#Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n = int(input('Digite um número: '))
n1 = int(input('Digite mais um número: '))

print('\033[31m*\033[m' * 30)
finalizando = 5#o professo colocou variante opção = 0
while finalizando == 5: # opção != 0
    print('''Escolha a opção que deseja:
    \033[32m[1] somar
    [2] multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\033[m''')
    print('\033[31m*\033[m' * 30)
    escolha = int(input('Qual é a sua escolha: ')) #A variante é opção em vez de escolha
    if escolha == 1:
        print('Somando \033[34m{} + {} = {}\033[m.'.format(n, n1, n + n1))
    elif escolha == 2:
        print('Multiplicando \033[36m{} x {} = {}\033[m.'.format(n, n1, n * n1))
    elif escolha == 3:
       if n > n1:
           print('O número maior é \033[35m{}\033[m.'.format(n))
       elif n1 > n:
           print('O número maior é \033[35m{}\033[m.'.format(n1))
    elif escolha == 4:
        n = int(input('Digite um número: '))
        n1 = int(input('Digite mais um número: '))
    elif escolha == 5:
        finalizando += 1
        print('\033[33mFinalizando programa ', end=''), sleep(1), print('.', end='')\
            , sleep(1), print('.', end=''), sleep(1), print('.\033[m')
    else:
        print('Opção incorreta!!! Digite novamente:')

#Mas o meu programa está funcionando perfeitamente e também está correto.