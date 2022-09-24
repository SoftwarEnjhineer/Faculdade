#Escreva um programa para informar o período de renovação dos exames da carteira de habilitação 
#com base na idade informada do motorista. Menores de idade não possuem carteira. 
#Até 65 anos, os exames devem ser renovados a cada 5 anos. Após 65 anos, os exames devem ser renovados a cada 3 anos
idade = int(input('Digite sua idade: '))
if (idade  <18):
    print('Você não tem habilitação')
if (idade >=18) and (idade <=65):
    print('A renovação é a cada 5 anos')
if (idade >65):
    print('A renovação é a cada 3 anos')
