#Exercício 29 – Radar eletrônico

#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

carro = float(input('Qual é a velocidade do carro? KM '))
print('A velocidade do carro é {} km/h.'.format(carro))
if carro > 80:
    velocidade = carro - 80
    multa = velocidade * 7.00
    print('Você foi multado! Você ultrapassou {}km/h. \nSua Multa vai ser do valor de R${:.2f}.'
    .format(velocidade, multa))
else:
    print('Parabéns! Continue dirigindo com segurança !')
#Este execício pode ser feito sem o else, tirando o else e utilizando somente o if, é uma condição simples.
#nesse caso você vai colocar um print mostrando 'Tenha uma boa viagem, Dirija coom segurança' e assim vai aparecer isso para ambos.
#e não vai precisar do else, e nem vai desejar parabéns.