#Exercício 7 – Média Aritmética

#Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a sua média:

nota1 = float(input('Digite a 1° nota do aluno: '))
nota2 = float(input('Digite a 2°̣ nota do aluno: '))
resultado = (nota1 + nota2) / 2
print('A primeira nota do aluno é {}'
     ' \nA segunda nota do aluno {}'
     ' \nA média de nota deste aluno é {:.1f}'.format(nota1, nota2, resultado))

#neste exercício você tem que seguir a ordem de precedência para fazer os calculos, a explicação está na
#apostila.