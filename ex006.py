#Exercício 6 – Dobro, Triplo, Raiz Quadrada
#Crie um algoritmo que leia um número e mostre o seu dobro,
#triplo e raiz quadrada:

n = int(input('Digite um número: '))
print('O número que você digitou é {}.'.format(n))
print('O dobro dele é {}'.format(n * 2))
print('O triplo dele é {}'.format(n * 3))
print('A Raiz quadrada dele é {:.2f}'.format(n ** (1/2)))

#Este exercício pode ser feito com a função pow(), para calcular a raiz quadrada.