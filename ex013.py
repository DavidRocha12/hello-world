#Exercício 13 – Reajuste Salarial

#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento:

salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('O salário do funcionário é R${:.2f} e com 15% de aumento '
      'o salario vai ser R${:.2f}.'.format(salario, aumento))