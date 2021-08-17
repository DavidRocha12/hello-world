#Exercício 8 – Conversor de Medidas

#Escreva um programa que leia um valor em metros
#e o exiba convertido em centímetros e milímetros:

m = float(input('Digite uma distância em mêtros: '))
print('O valor que você digitou é {}M \ne convertido em:'.format(m))
cm = m * 100
mm = m * 1000
hm = m / 100
km = m / 1000
dam = m / 10
dm = m * 10
print('{:.0f} cm - centimetros'.format(cm))
print('{:.0f} mm - Milimetros'.format(mm))
#Neste exercício o professor converte tambèm:
print('{} hm - hectomêtro'.format(hm))
print('{} km - kilomêtro'.format(km))
print('{} dam - decametros'.format(dam))
print('{:.0f} dm -diametros'.format(dm))
