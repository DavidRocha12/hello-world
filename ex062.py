#Exercício 62 – Super Progressão Aritmética v3.0

#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Progressão aritmética 3.0')
print('')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
pa = 1
continuar = 10#fazendo a variante continuar você vai simular que o programa vai mostrar os 10 primeiros termos.
total = 0 #aqui o total de termos mostra que começa no 0
while continuar != 0:
    total = total + continuar #aqui o total = total valendo 0 mais o continuar que é 10, então o total vai
    #estar valendo 10 que é a quantidade de termos que vai mostrar no inicio.
    while pa <= total:#aqui no exercício 61 é 10, então foi criado uma variável para mostrar o total de termos.
        print('{} -> '.format(termo), end='')
        termo += razao
        pa += 1
    print('Pausa')
    continuar = int(input('Quantos termos a mais você deseja: '))
    #perguntando e digitando o número, por causa da variante total= total + continuar, ele vai te mostra quantidade de
    #termos que você digitou.
print('Progresão finalizada com {} termos.'.format(total))#fazendo o print total ele vai te mostra a quantidade
#de termos que foi mostrado.
print('Fim')

#Na programação você pode utilizar while dentro de while, for dentro de for e if dentro de if,
#condições de repetição também pode ser utilizado como uma condição aninhada,
#você pode utilizar da forma que você quiser.