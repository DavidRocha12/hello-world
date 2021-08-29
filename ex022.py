#Exercício 22 – Analisador de Textos

#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras aotodo(sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome inteiro: '))
print('Seu nome em letra maiúscula fica ({}).'.format(nome.upper()))
print('Seu nome com letra minúscula fica ({}).'.format(nome.lower()))
#lista = nome.split()
print('O seu nome completo  tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('O seu nome completo tem {} letras'.format(len(''.join(lista))))
print('O seu Primeiro nome tem {} letras.'.format(nome.find(' ')))
#print('O seu primeiro nome tem {} letras.'.format(len(lista[0])))

#A FORMA QUE ESTÁ APAGADO É O MODO QUE O PROFESSOR FEZ E O QUE ESTÁ ATIVO É DA FORMA QUE FIZ.
