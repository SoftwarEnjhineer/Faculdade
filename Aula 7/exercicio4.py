#Escreva um programa em linguagem python que leia a idade, a altura e o peso de 5 pessoas.
#O programa deve calcular e mostrar:
#a. A quantidade de pessoas com idade superior a 50 anos.
#b. A altura média das pessoas com idade entre 10 e 20 anos.
#c. O percentual de pessoas com peso inferior à 60 quilos.

quantPessoas = 10

quantPessoasSup50 = 0
somaAltura = 0
quantPessoas10a20 = 0
quantPessoasMenor60Kg = 0
media = 0

for i in range(0, quantPessoas):
    print('Pessoa numero:', i + 1, '\n')

    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    peso = int(input('Digite o peso: '))

    print('\n')

    if idade > 50:
        quantPessoasSup50 += 1

    if idade >= 10 and idade <= 20:
        somaAltura += altura
        quantPessoas10a20 += 1

    if peso < 60:
        quantPessoasMenor60Kg += 1

if quantPessoas10a20 > 0:
    media = somaAltura / quantPessoas10a20

print(f'Quantidade de pessoas com idade superior a 50 anos: {quantPessoasSup50}\n')

print(f'A altura média entre 10 e 20 anos: {media}\n')

print('O percentual de pessoas com peso inferior à 60 quilos: ' +
format(quantPessoasMenor60Kg * 100 / quantPessoas, '.2f'))
