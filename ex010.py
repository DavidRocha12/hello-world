#Exercício 10 – Conversor de Moedas

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar:
#considere que U$1.00 custa R$3.27

carteira = float(input('Quantos de dinheiro você tem na Carteira? R$ '))
dolar = carteira / 3.27
print('O valor que você tem é R${:.2f}, convertendo para dolar você tem U$ {:.2f}'.format(carteira, dolar))
