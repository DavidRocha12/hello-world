#Exercício 14 – Conversor de Temperaturas

#Escreva um programa que converta uma temperatura digitando em graus Celsius
#e converta para graus Fahrenheit:

c = float(input('Qual é o valor em graus celsius? '))
f = (c / 5) * 9 + 32 #essa é a formula para fazer a conversao de celsius para fahrenheit.
print('O valor é {}°C , convertendo para graus fahrenheit o valor é {:.1f}°F.'.format(c, f))
