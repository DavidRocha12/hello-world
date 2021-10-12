#Exercício 37 – Conversor de Bases Numéricas

#Escreva um programa em Python que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.
print('*' * 10, 'Conversão Bases Númericas', '*' * 10)

n = int(input('Digite um Número: '))

print('Escolha a conversão que deseja: ')
print('Digite 1: Binário')
print('Digite 2: Octal')
print('Digite 3: hexadecimal')
escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    c = bin(n)
    b = 'Binário'
elif escolha == 2:
    c = oct(n)
    b = 'Octal'
elif escolha == 3:
    c= hex(n)
    b = 'Hexadecimal'
print('O seu número é {} e ele convertido para {} é {}.'.format(n, b, c[2:]))
