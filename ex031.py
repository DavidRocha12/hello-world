#Exercício 31 – Custo da Viagem

#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
#até 200Km e R$0,45 para viagens mais longas.

v = float(input('Quantos km é a sua viagem? Km '))

if v <= 200:#se o valor for menor ou igual a 200 a resposta vai ser esta.
    valor = v * 0.50#Calculo para saber o custo da viagem
else:# se for acima de 200 vai ser esta.
    valor = v * 0.45 #CAlculo para saber o custo da Viagem.
print('Sua Viagem é de {}km, e vai ter um custo de R${:.2f}'.format(v, valor))

#neste exercício você pode colocar com uma condição simplificada também.
#ex: valor = v * 0.50 if v <= 200 else valor v * 0.45