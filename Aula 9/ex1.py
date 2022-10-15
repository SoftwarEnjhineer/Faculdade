# 1) Teste todos os exemplos dos slides.

lista = []
print(lista)


lista = ['O carro','peixe',4444,164]
print(lista)


novaLista = ['pedra',lista]
print(novaLista)

print(lista[0])
print(lista[2])


print(len(novaLista))


print('peixe' in lista)
print('gato' in lista)


numeros = [44.44, 55, 44, 4444, 9879]

print(min(numeros))
print(max(numeros))
print(sum(numeros))


linguagensProgramação = ['Java','SqlServer','Deplhi','Python']
linguagensProgramação.append('Android')
print(linguagensProgramação)


linguagensProgramação = ['Java','SqlServer','Deplhi','Python']
linguagensProgramação.insert('Oracle')
print(linguagensProgramação)


livros = ['Java','C','Pascal','Python','HTML']
print(livros)
livros.pop()
print(livros)

livros.pop(1)
print(livros)


linguagensProgramação = ['Oracle','Java','SqlServer','Deplhi','Python','Android','Oracle']
linguagensProgramação.remove('Oracle')

print(linguagensProgramação)


linguagensProgramação = ['Java','SqlServer','Deplhi','Python','Android','Oracle']
linguagensProgramação.remove('Oracle')

print(linguagensProgramação)

# linguagensProgramação = ['Java','SqlServer','Deplhi','Python','Android']
# linguagensProgramação.remove('Oracle')
# Causa erro 

linguagensProgramação = ['Java','SqlServer','Deplhi','Python','Android']
linguagensProgramação.reverse()

print(linguagensProgramação)


linguagensProgramação = ['Java','SqlServer','Deplhi','Python','Android']
linguagensProgramação.sort()

print(linguagensProgramação)


linguagensProgramação = ['Oracle','Java','SqlServer','Deplhi','Python','Android','Oracle']

linguagensProgramação.count('Python')
print(linguagensProgramação)

linguagensProgramação.count('Oracle')
print(linguagensProgramação)


x = [1,2,3,4,5]

if 4 in x:
    print('Está contido')


x = [1,2,3,4,5]

if 8 not in x:
    print('Está contido')
