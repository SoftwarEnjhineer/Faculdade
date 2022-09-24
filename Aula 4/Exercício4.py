#4 - Escreva um programa que leia dois números inteiros e apresente o resultado correspondente à operação 
#escolhida pelo usuário. As operações disponíveis serão:  

#A média aritmética dos dois números  

#A diferença entre eles  

#O produto dos dois números.
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
operação = int(input('Escolha a operação, Digite 1 para Média aritmética, 2 para a diferença e 3 para produto.\n'))
if operação == 1:
    print('A média aritimética é:',(numero1+numero2) /2)
if operação ==2:
    print('A diferença é:', numero1 - numero2)
if operação ==3:
    print('O produto é:', numero1 * numero2)
