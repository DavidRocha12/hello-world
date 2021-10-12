#Exercício 57 – Validação de Dados

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('''Digite "M" para masculino ou "F" para feminino.''')
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é seu sexo? ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
       print('Informação errada, tente Novamente!')
if sexo == 'M':
    print('Seu sexo é Masculino!')
elif sexo == 'F':
    print('Seu sexo é Feminino!')

#exercício da forma que o professor fez:

sexo = str(input('Informe seu sexo: (M/F) ')).strip().upper()[0]#neste aqui foi utilizado fatiamento de string
#se digitar masculino vai aparecer somente o M
while sexo not in 'MF': #enquanto sexo não for MF
    sexo = str(input('Dados inválidos, informe seu sexo: (M/F) ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

#forma do professor mais simples e prático,
#mas da forma que fiz também está certo, e o exercício foi feito antes de ter visto o video.
