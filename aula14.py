'''for c in range(1, 10): #condição de repetição for, exemplo para explicação da aula 14
    print(c)
print('acabou!!!')'''

c = 1 #O c(contador) começa com 1, que é o inicio desse range
while c < 10:#aqui é enqunto o c(contador) for menor que 10
    print(c)
    c += 1#contador c += 1 nesse caso tem que ser colocado depois do print,
    # se colocar antes ele começa a contar apartir do 2
print('Acabou!!!')

#o While se eu sei o limite ou não sei o limite eu posso usar o while, se eu sei o limite você pode
#usar o for se você não sabe o limite você naõ pode usar o for.
#sabendo o limite você pode usar o for ou o while, se você não sabe o limite, pode usar somente o while.

n = 1#O n começa com 1, sempre é necessário começar um contador
while n != 0:#o n != 0 pode ser chamado de condição de parada(flag)
    #enquanto p n for diferente de 0 ele não vai parar de fumcioner, se digitar o 0 o programa vai finalizar
    n = int(input('digite um valor: '))
print('Fim')
#Nesse caso se o zero for digitado primeiro ele ja vai finalizar o programa.

r = 'S' #o inicio é S
while r == 'S': #enquanto a resposta for == a sim o programa vai continuar
    n = int(input('Digite um valor: '))# ele vai ler um valor
    r = str(input('Quer continuar S/N: ')).upper()#e vai perguntar se que contimuar. se colocar não ele finaliza.
print('Fim')

#por exemplo se for pedir para um programa perguntar a idade de 50 pessoas, o certo é utilizar o for, se não sabe
#quantas pessoas vai ser perguntado a idade é necessário usar o while.
#se vc não sabe quantas pessoas são tem que utilizar o while
#for e while são estruturas de repetição para situações diferentes.

n = 1# Número vai receber 1
par = impar = 0 # se você quiser fazer assim, o programa funciona perfeitamente, no caso esse vai ser um contador
while n != 0: #enquanto n for diferente de 0
    n = int(input('Digite um número: '))
    if n != 0: # se n for diferente de 0 - isso serve para não considerar um zero como par, porque ele é considerado
        #um núnero nulo
        if n % 2 == 0:# se n for divisivel 2 == 0 - para ver se o número é par
           par += 1 #contador par
        else: #se não é impar
            impar += 1 #contador impar
print('Você digito {} números pares, e {} números impares.'.format(par, impar))#aqui vai mostrar quantos
#números pares e quantos números impares você digitou, e se você digitar o 0, você finaliza o programa.