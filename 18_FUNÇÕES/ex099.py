def maiorf(*num):
    print('=-=' * 30)
    print('Analisando os valores passados...')
    maior = 0
    casas = len(num)
    for n in num:
        print(f'{n}', end=' ')
        if casas == 0:
            maior = n
        if casas > 0 and n > maior:
            maior = n
    print(f'foram informados {casas} valores ao total.')
    print(f'O maior valor foi {maior}')
        

maiorf(2,9,4,5,7,1)
maiorf(4,7,0)
maiorf(1,2)
maiorf(6)
maiorf(0)