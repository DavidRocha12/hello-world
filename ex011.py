#Exercício 11 – Pintando Parede

#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados:

a = float(input('Qual é a altura da parede: '))
l = float(input('Qula é a largura da parede: '))
m = a * l #aqui utilizei uma variável para multiplicar, para saber o metro quadrado.
tinta = m / 2 #aqui utilizei uma variável para dividir
print('A largura da parede é {}m, e a altura é {}m.'.format(l, a))
print('O metro quadrado da parede é {}M², e vai utilizar {} litro(s) de tinta.'.format(m, tinta))
