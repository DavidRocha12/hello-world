#Exercício 20 – Sorteando uma ordem na lista

#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Digite o nome do 1° aluno: ')).strip().upper()
a2 = str(input('Digite o nome do 2° aluno: ')).strip().upper()
a3 = str(input('Digite o nome do 3° aluno: ')).strip().upper()
a4 = str(input('Digite o nome do 4° aluno: ')).strip().upper()
lista = [a1, a2, a3, a4]
ordem = shuffle(lista)#shuffle significa embaralhar, colocar a lista entre parenteses, mas no print colocar a lista,
# e assim vai mostrar a lista embaralhado.
print('A ordem de apreserntação dos alunos é {}'.format(lista))
