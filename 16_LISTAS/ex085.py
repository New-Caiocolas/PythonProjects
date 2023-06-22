lista = [[],[]]
for n in range(0,7):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Todos os valores {lista}')
print(f'Valores ímpares {lista[1]}')
print(f'Valores pares {lista[0]}')