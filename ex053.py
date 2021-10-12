#Exercício 53 – Detector de Palíndromo

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
lista = frase.split()
juntar = ''.join(lista)
cont = ''
for contra in range(len(juntar) -1, -1, -1):
    cont += juntar[contra]
print('A frase é {} e essa frase ao contrário fica {}.'.format(juntar, cont))
if juntar == cont:
    print('Esta palavra é um palindromo!!!')
else:
    print('ESta frase não é um Palindromo!!!')
