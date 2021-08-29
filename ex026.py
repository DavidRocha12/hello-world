#Exercício 26 – Primeira e última ocorrência de uma string:

#Faça um programa que leia uma frase pelo teclado
#e mostre quantas vezes aparece a letra “A”,
#em que posição ela aparece a primeira vez
#e em que posição ela aparece a última vez:

frase = str(input('Digite uma frase: ')).strip().upper()
print('O sua frase é {}, e aparece {} vezes a letra "A".'.format(frase, frase.count('A')))
print('A primeira letra "A" esta na posição {}.'.format(frase.find('A')+1))
print('A ultima letra "A" está na posição {}.'.format(frase.rfind('A')+1))