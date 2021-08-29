#Exercício 34 – Aumentos múltiplos

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
#o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: R$'))

if salario <= 1250.00:
    valor = 15#Coloquei essa variável para mostrar a porcentagem
    aumento = salario + (salario / 100 * 15)#Variável para calculo do aumento de salário.

else:
    valor = 10
    aumento = salario + (salario / 100 * 10)

print('O salário do funcionário é R${:.2f}, e com {}% de aumento fica R${:.2f}.'
      .format(salario, valor, aumento))
