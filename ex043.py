#Exercício 43 – Índice de Massa Corporal

#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Qual é o seu peso? kg'))
altura = float(input('QUal é a sua altura? '))
print('')
imc = peso / (altura ** 2)# Formula para saber o índice de média corporar.
print('O seu peso é {}kg e a altura é {}, e seu IMC(Indice de massa corporal) é {:.1f}'
      .format(peso, altura, imc))
if imc < 18.5:#Condição aninhada para saber categoria do imc.
    print('Você está abaixo do peso !'
          '\nProcure um médico.')
elif imc == 18.5 or imc < 25:
    print('Seu peso está ótimo !!!'
          '\nContinue assim !')
elif imc == 25 or imc < 30:
    print('Você está um pouco acima do peso(Sobrepeso) !'
          '\nFaça mais exercícios !!!')
elif imc == 30 or imc < 40:
    print('Você está acima do peso (Obesidade) !'
          '\nProcure um médico !!!')
else:
    print('Você está muito acima do peso (Obesidade Mórbida) !!!'
          '\n Procure um médico imediatamente !')
