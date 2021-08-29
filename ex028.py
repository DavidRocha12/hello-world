#Exercício 28 – Jogo da Adivinhação v.1.0


#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep #biblioteca time, para colocar tempo no seu programa.
n = int(input('Adivinhe qual número o computador escolheu. entre 0 a 5: '))#aqui o jogador tenta adivinhar qual número é.
número = randint(0,5)#Faz o computador pensar.
print('Processando ...')
sleep(3)#sleep é um método que faz o computador pausar por alguns segundos, os segundo é estipulado pelo programador.
print('O seu número é {} e o computador escolheu {}.'.format(n, número))
if n == número: #Aqui o jogador acertou.
    print('Parabéns! você adivinhou o número do computador, você venceu !!!')
else:#Aqui o jogador errou.
    print('Que pena, não é o mesmo número, você perdeu !!!')
