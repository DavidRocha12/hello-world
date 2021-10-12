#Exercício 58 – Jogo da Adivinhação v2.0

#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('tente adivinhar o número que o computador vai escolher de 0 á 10:')
n = int(input('Digite um número: '))
pc = randint(1, 10)
print('')
cont = 1# O meu programa tive que colocar o 1 porque 0 não estava contando o 1° n.
while n != pc: #condição de repetição while
    n = int(input('Você não acertou, tente novamente!!! \nDigite um número: '))
    cont += 1
    print('')
if n == pc:#condição simples
    print('Parabéns você conseguiu adivinhar!!!')
    print('O número que o computador escolheu é {}.'.format(pc))
    print('Foi necessário {} vezes para você adivinhar o número.'.format(cont))
print('')
#forma que o professor fez está abaixo, mas o meu também está correto.

from random import randint#Biblioteca random, ramdint para números aleatórios

computador = randint(1, 10)
print('Sou seu Computador...')
print('Acabei de pensar em um número entre 0 e 10. \nSerá que você sabe adivinhar qual é?')
acertou = False# o professor fez uma variável falando que é falso
palpites = 0#contador palpites

while not acertou:# aqui o professor coloca que enquanto não acertou ele continua perguntando.
    jogador = int(input('qual é seu palpite? '))
    palpites += 1 #psrs fszer s contagem
    if jogador == computador:#se o jogador for igual ao computador
        acertou = True #e dentro da condição simples ele fez uma variavel verdadeiro;
    else: #se não, o programa vai te falando se o número é maior ou menor do que vc digitou.
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas, parabéns !!!'.format(palpites))

