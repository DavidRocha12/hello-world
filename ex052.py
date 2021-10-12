#Exercício 52 – Números primos

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('Números Primos')
print('')
n = int(input('Digite um número: '))
print('')
cont = 0 #serve para contar quantas vezes o número pode ser divisivel.

for p in range(1, n + 1):#repetição para fazer a contagem do 1 até o número que foi digitado.

    if n % p == 0:# se o número for divisivel pelo contador p igual a 0, isso é para facilitar e mostrar
        #quantas vezes o número é divisivel, e foi colocado cores abaixo para saber por quais números o seu número
        #é divisivel
        cont += 1
        print('\033[34m{}\033[m'.format(p), end=' ')#cor azul para mostrar os números que é divisivel
    else:
        print('\033[31m{}\033[m'.format(p), end=' ')#cor vermelho para números que não é divisivel

print('\nO número {} pode ser divisivel {} vezes.'.format(n, cont))

if cont == 2:#se o número foi divisivel até duas vezes, ele é um número primo
    print('É um número primo!!!')
else:#se for divisivel por mais ele não é um número primo
    print('Não é um número primo!!!')