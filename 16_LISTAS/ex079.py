lista = []
while True:
    v = int(input('digite um valor:'))
    if v not in lista:
        lista.append(v)
    x = str(input('Quer continuar S/N: '))
    if x in 'Nn':
        break
print(sorted(lista))