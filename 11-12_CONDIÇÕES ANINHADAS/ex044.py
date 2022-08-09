print('======== lojas caiocolas ========')
compras = float(input('PREÇO DAS COMPRAS:R$'))
print('''processando...
[1] a vista dinheiro/pix
[2] a vista no cartão
[3] 2x cartão
[4] 3x ou mais no cartão''')
op = int(input('OPÇÃO:'))
pix10 = compras - (compras * 10 / 100)
cartao5 = compras - (compras * 5 / 100)
cartao2x = (compras / 2)
cartao20 = compras + (compras * 5 / 100)
if op == 1:
    print('A vista no dinheiro/pix vai custar R${}'.format(pix10))
elif op == 2:
    print('A vista no cartão vai custar R${}'.format(cartao5))
elif op == 3:
    print('Em 2x no cartão vai custar R${} durante dois meses, total {} reais'.format(cartao2x,compras))
elif op == 4:
    print('''você deseja dividir de quantas vezes
    [1]3x 20% juros
    [2]4x 20% juros
    [3]5x 20% juros
    [4]6x 20% juros
    [5]7x 20% juros
    [6]8x 20% juros
    [7]9x 20% juros
    [8]10x 20% juros''')
    div = int(input('OPÇÃO:'))
    cartao3x = (cartao20 / 3)
    cartao4x = (cartao20 / 4)
    cartao5x = (cartao20 / 5)
    cartao6x = (cartao20 / 6)
    cartao7x = (cartao20 / 7)
    cartao8x = (cartao20 / 8)
    cartao9x = (cartao20 / 9) 
    cartao10x = (cartao20 / 10)
    if div == 1:
        print('Em 3x no cartão vai custar R${} durante 3 meses'.format(cartao3x))
    elif div == 2:
        print('Em 4x no cartão vai custar R${} durante 4 meses'.format(cartao4x))
    elif div == 3:
        print('Em 5x no cartão vai custar R${} durante 5 meses'.format(cartao5x))
    elif div == 4:
        print('Em 6x no cartão vai custar R${} durante 6 meses'.format(cartao6x))
    elif div == 5:
        print('Em 7x no cartão vai custar R${} durante 7 meses'.format(cartao7x))
    elif div == 6:
        print('Em 8x no cartão vai custar R${} durante 8 meses'.format(cartao8x))
    elif div == 7:
        print('Em 9x no cartão vai custar R${} durante 9 meses'.format(cartao9x))
    elif div == 8:
        print('Em 10x no cartão vai custar R${} durante 10 meses'.format(cartao10x))
    else:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
    