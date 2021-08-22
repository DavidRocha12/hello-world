#Exercício 18 – Seno, Cosseno e Tangente

#Faça um programa que leia um ângulo qualquer
#e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan
a = float(input('Digite qualquer ângulo: '))
ar = radians(a)#para calcular o seno, cosseno e tangente com a biblioteca math tem que transformar o ângulo
#em radianos
print('O ângulo {}, tem o seno de {:.2f}'.format(a, sin(ar)))#formula para saber o seno de radianos.
print('O ângulo {}, tem o cosseno de {:.2f}'.format(a, cos(ar)))#formula para saber o cosseno de radianos.
print('O ângulo {}, tem o a tangente de {:.2f}'.format(a, tan(ar)))#formula para saber a tangente de radianos.
