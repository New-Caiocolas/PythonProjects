lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    con = str(input('Quer continuar S/N: '))
    if con in 'Nn':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('=-' * 20)
print(f'Sua lista é {lista}')
print(f'Os números pares: {par}')
print(f'Os número impares: {impar}')

