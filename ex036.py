#Exercício 36 – Aprovando Empréstimo

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor do seu financiamento? R$'))#valor da residência para fazer o financiamento
anos = int(input('Quantos anos vai ser seu financiamento? '))#quantidade de anos para o financiamento
salario = float(input('Qual é o valor do seu salário? R$'))#salário comprador

print('')

parcela = casa / (anos * 12)#calculo para transformar anos em meses e dividir o valor da casa com as quantuidades de meses
adiantamento = salario * 30 / 100#Calculo para saber 30% do salario do comprador

print('O valor do seu financiamento é de R${:.2f}, o tempo de financiamento vai ser de {} anos,'
      ' \ne a parcela vai ser de R${:.2f}.'.format(casa, anos, parcela))

if adiantamento < parcela:#se 30% do salário do comprador for menor que parcelas mensais
    print('Financiamento Negado ! O seu salário não é compatível para este financiamento!!!')
else:#se os 30% do salário for maior que as parcelas
    print('Parabéns!!! Seu Financiamento foi aprovado!!!')
#Fiz exercício para treinar, utilizei somente o if e o else, sem necessidade de utilizar o elif.
#Na apostila está feito com elif, o professor também fez somente com o if e o else.
