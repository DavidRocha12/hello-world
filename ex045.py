#Exercício 45 – GAME: Pedra Papel e Tesoura

#Crie um programa que faça o computador jogar Jokenpô com você:
from random import randint
from time import sleep

from random import randint#Biblioteca Random
from time import sleep#biblioteca time e função sleep para colocar tempo para item aparecer.
escolha = ('Pedra', 'Papel', 'Tesoura') # é necessário colocar itens entre parenteses, mais para frennte
# isso será explicado.
computador = randint(0, 2)#funçõa para a escolha de nṕumero aleatório
print('''### Jogo Jokenpô ###
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Faça sua Jogada: '))
print('')
print('Jo...', end=''), sleep(2), print('Ken...',end=''), sleep(2), print('Pô'), sleep(2)
print('')

print('O computador escolheu {}.'.format(escolha[computador]))
if jogador > 2:# condição composta para mostrar se o jogador jogou certo ou não.
    print('Jogada invalida, jogue novamente!!!')
else:
    print('Você escolheu {}. '.format(escolha[jogador]))

print('')

if jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
    print('Computador Ganhou !!!')
elif jogador == 1 and computador == 0 or jogador == 2 and computador == 1 or jogador == 0 and computador == 2:
    print('Você ganhou !!!')
elif jogador == 0 and computador == 0 or jogador == 1 and computador == 1 or jogador == 2 and computador == 2:
    print('Foi empate!!!')

# Na condição aninhada o professor faz o if se o computador escolher o número, dentro desse if tem outro if com as
#opções do jogador se com o print se o computar vence, perde ou ganha, mas o meu jeito também esá certo.