#Exercício 63 – Sequência de Fibonacci v1.0

#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
#e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

#0 – 1 – 1 – 2 – 3 – 5 – 8
print('Sequência fibonacci 1.0')
print('')
n = int(input('Digite um número: '))
t1 = 0#primeiro termo definido automaticamente
t2 = 1#segundo termo definido autiomáticamente
print('{} - {} - '.format(t1, t2), end ='')
cont = 3#o contador vai começar em 3, porque eu já mostrei o primeiro e segundo termo.
while cont <= n:#enquanto meu contador for menor ou igual ao n
    t3 = t1 + t2 #o temo 3 vai ser igual o t1 + o t2
    print('{} - '.format(t3), end='')
    t1 = t2#aqui o t1 passa a ser o t2
    t2 = t3#aqui o t2 passa a ser o t3, iso para poder ir somando
    cont += 1 #contador recebendo ele + 1 para ir contando
print('Fim')