#Exercício 48 – Soma ímpares múltiplos de três

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
#e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for calculo in range(1, 501, 2):
    if calculo % 3 == 0:
        cont += 1
        soma += calculo
print('A quantidade de números impares multiplo de 3 é {}, e a soma deles é {}'.format(cont, soma))

# este exercício, os comentários estão na apostila do mundo 2, explicando sobre cada item.