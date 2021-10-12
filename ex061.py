#Exercício 61 – Progressão Aritmética v2.0

#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Progressão Aritmética 2.0')
print('')
termo = int(input('Qual é o Primeiro Termo: '))
razao = int(input('Qual é a Razão da PA: '))
pa = 0 #contador, aqui começa com 0, mas tem que ficar antes do print, se não ele começa mostrando apartir
#do 2 termo.
print('Os 10 primeiros termos de uma PA é: ', end='')
while pa < 10:
    pa += 1# Explicação acima sobre o contador.
    soma = termo + (pa - 1) * razao#Eu utilizei essa formula para resolver a pa
    print('{} -> '. format(soma), end='')
print('Fim')
print('')

#programa feito pelo professor:
print('Gerador de Pa:')
print('=/-' * 10)
primeiro = int(input('Qula é o Primeiro Termo: '))
razao = int(input('Qual é a razão: '))
termo = primeiro #aqui o professor fez o primeiro ser o termo
cont = 1 #aqui o professor coloca 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    cont += 1# e colaque i contador depois do print, se colocar 0 no cont e cont += 1 ele vai começar a contar
    #após o 2 digito do primeiro termo.
    termo += razao #e aqui calcula o termo(primero) + a razão, que se você colocar no primeiro = 0 e a razão
    # = 5, o programa vai pular de 5 em 5 até 10 vezes.
print('Fim')
