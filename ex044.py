#Exercício 44 – Gerenciador de Pagamentos

#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

produto = float(input('Qual é o valor do produto? R$'))
print('')
print('Digite a forma de pagamento é a Cartão, Dinheiro ou Cheque:')
pagamento = str(input('Qual é a forma de pagamento? ')).strip().upper()
print('')

if pagamento == 'DINHEIRO' or pagamento == 'CHEQUE':
    porcentagem = '10'
    desconto = produto - (produto * 10 / 100)
    print('O valor do produto é R${:.2f}'.format(produto))
    print('E com desconto de {}% o produto vai ser R${:.2f}.'.format(porcentagem, desconto))

elif pagamento == 'CARTÃO' or pagamento == 'CARTAO':
    parcela = str(input('É á vista ou á prazo? ')).strip().upper()

    if parcela == 'Á VISTA' or parcela == 'A VISTA':
        porcentagem = '5'
        desconto = produto - (produto * 5 / 100)
        print('O valor do produto é R${:.2f}'.format(produto))
        print('E com desconto de {}% o produto vai ser R${:.2f}.'.format(porcentagem, desconto))
    elif parcela == 'Á PRAZO' or parcela == 'A PRAZO':
        quantidade = int(input('Em quantas vezes no cartão? '))
        prazo = produto / quantidade

        if quantidade == 2:
            print('')
            print('O valor do produto é R${:.2f}'.format(produto))
            print('O produto em {}x sem juros no cartão vai ficar R${:.2f} cada parcela.'.format(quantidade, prazo))
        elif quantidade >= 3:
            juros = (produto + (produto * 20 / 100)) / quantidade
            print('O valor do produto é R${:.2f}'.format(produto))
            print('Com 20% de juros o produto vai fcar no valor de R${:.2f}.'
                  .format(produto + (produto* 20 / 100)))
            print('O Produto parcelado em {}x vai ter um custo de R${:.2f} cada Parcela.'
                  .format(quantidade, juros))

#Este exercício o professor coloca a opção de 1 ao 4 para escolher a forma de pagamento, e opçõa invalida se alguem digitar
# uma opção que não existe.
#O meu exercício está certo e funcionando, mas o do professor é bem mais simples.
