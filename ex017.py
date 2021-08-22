#Exercício 17 – Catetos e Hipotenusa

#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h =hypot(ca,co)
#q = (co ** 2) + (ca ** 2)#Essa é a formula para saber a hipotenusa sem a biblioteca
#h = q ** (1/2)
print('Calculando o {} CO e o {} CA, o resultado é o comprimento da hipotenusa que é {:.2f}.'.format(co, ca, h))
