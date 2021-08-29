#Exercício 24 – Verificando as primeiras letras de um texto:

#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()
print('O nome da sua cidade é {} e é {} que começa com "SANTO"'.format(cidade, cidade[:5] == 'SANTO'))