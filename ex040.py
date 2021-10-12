#Exercício 40 – Aquele clássico da Média

#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a 1° nota do aluno: '))
nota2 = float(input('Digite a 2° nota do aluno: '))

media = (nota1 + nota2) / 2

print('As notas do aluno é {} e {}, e sua média é {}'.format(nota1, nota2, media))

if media < 5.0:
    print('Aluno \033[31mREPROVADO\033[m!!!')
elif media <= 6.9:
    print('Aluno está em \033[33mRECUPERAÇÃO\033[m!!!')
elif media >= 7.0:
    print('Parabéns, aluno foi \033[34mAPROVADO\033[m!!!')