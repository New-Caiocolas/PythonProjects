c = ''
cont = 0
soma = 0
maior = 0
menor = 0
while c != 'N':
    n = int(input('digite um número:'))
    c = str(input('quer continuar:[S/N]')).strip().upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
print('vc digitou {} números e a media foi {:.2f}'.format(cont,soma / cont))
print('o maior valor é {} e o menor é {} '.format(maior,menor))