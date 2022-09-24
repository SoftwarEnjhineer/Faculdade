print('---Calculadora de peso ideal---')
altura = float(input('Qual sua altura? '))
sexo = int(input('Informe seu sexo\nDigite 1 para Homem\nDigite 2 para mulher\n'))
pesoHomem = (72.7 * altura) -58
pesoMulher = (62.1 * altura) -44.7
if (sexo == 1):
    print('Seu peso ideal é de {:.2f} kg'.format(pesoHomem))
elif (sexo == 2):
    print('Seu peso ideal é de {:.2f} kg'.format(pesoMulher))