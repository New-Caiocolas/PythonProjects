total = 0
maior = 0
nomevelho = ''
mulhernova = 0
for c in range(1, 5):
    print('----- {} PESSOA -----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    total += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if maior < idade and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        mulhernova += 1
media = total / 4
print('A media de idade do grupo é de {}'.format(media))       
print('O homem mais velho do grupo tem {} anos e o nome dele é {}'.format(maior, nomevelho))
print('Neste grupo existem {} mulheres com menos de 20 anos'.format(mulhernova))
