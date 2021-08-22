#Exercício 12 – Calculando Descontos

#Faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço, com 5% de desconto:

produto = float(input('Qual é o valor do Produto? R$'))
desconto = produto - (produto * 5 / 100) #esta formula é para fazer o calculo de porcentagem e tirar o desconto
#do valor
print('O valor do produto é R${:.2f} e com 5% de desconto vai ficar R${:.2f}.'.format(produto, desconto))
