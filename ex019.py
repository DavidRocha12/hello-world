#Exercício 19 – Sorteando um item na lista

#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos
#e escrevendo na tela o nome do escolhido.

from random import choice
a1 = str(input('Nome do 1° aluno: ')).strip().upper()
a2 = str(input('Nome do 2° aluno: ')).strip().upper()
a3 = str(input('Nome do 3° aluno: ')).strip().upper()
a4 = str(input('Nome do 4° aluno: ')).strip().upper()
lista = [a1, a2, a3, a4]#para poder fazer a escolha é necessário fazer uma variante lista, que para o python
# fica uma lista fica entre colchetes, e dentro desses colchetes fica quem vai participar da lista.
escolha = choice(lista)#
print('O nome do aluno escolhido é {}'.format(escolha))
