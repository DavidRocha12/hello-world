#Exercício 49 – Tabuada v.2.0

#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.

print('#' * 14, 'Tabuada 2.0', '#' * 14)
print('')
n = int(input('Digite o número da tabuada que deseja: '))
print('')
for tabuada in range(1, 11):
    print('{} x {:2} = {}'.format(n, tabuada, n * tabuada))
print('')
print('#' * 40)