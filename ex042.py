#Exercício 42 – Analisando Triângulos v2.0

#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('Analizando Triângulos 2.0')

print('')

r1 = float(input('Digite a 1° reta: '))
r2 = float(input('Digite a 2° reta: '))
r3 = float(input('Digite a 3° reta: '))

print('As retas {}, {} e {},'.format(r1, r2, r3))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:#Condição composta para saber se formam um triângulo.
    print('Formam um triângulo !')
    if r1 == r2 and r1 == r3 and r2 == r3:#Condição aninhada dentro da condição composta para saber os tipos de triângulos.
        print('Todas as retas são iguais e este Triângulo é Equilátero !')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Duas retas são iguais e uma diferente e este Triângulo é Isósceles !')
    else:
        print('Todas as retas são diferentes e este Triângulo é Escaleno !')

else:
    print('Não Formam um triângulo !')

