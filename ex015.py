#Exercício 15 – Aluguel de Carros

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km percorridos o carro fez? Km '))
dias = int(input('Por quantos dias o carro foi alugado? '))
aluguel = dias * 60.00
kmrodados = km * 0.15
total = aluguel + kmrodados
print('São {} de viagem , e os kms rodados são {} km, '
      'tendo um custo de R${:.2f} de aluguel.'.format(dias, km, total))
