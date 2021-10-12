#Exercício 60 – Cálculo do Fatorial

#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

#5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para calcular seu fatorial: '))
print('{}! = '.format(n), end='')
c = n #começar o contador com o número digitado
f = 1 #começar variante com 1 para multiplicar
while c > 0: #enquanto o contador for maior do que 0 ele continua
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='') # se c for menor que 1 mostrar o x se não moatrar =
    f *= c #f vezes f = c, esse tem que vir antes do contador, se colocar depois o resultado vai dar 0
    c -= 1# tirar um do c para contar de traz para frente
print(' {}'.format(f), end='')
# para somar um número tem que comesar uma variante de soma com 0, se você quer multiplicar tem que começar com 1
#este exerçicio pode sr feito com o for, e o resultado pode ser feito com a biblioteca factorial.
#o while pode ser utilizado se eu sei o limite ou não e o for somente quando sei o limite.

