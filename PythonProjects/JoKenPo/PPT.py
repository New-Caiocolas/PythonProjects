import random
import time

print('jo ken po')
print('''[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jkp = ['PEDRA', 'PAPEL', 'TESOURA']
lista = [0,2]
bot = random.choice(lista)
jogada = int(input('digite a sua jogada:'))
print('jo')
time.sleep(1)
print('ken')
time.sleep(1)
print('po!!!')
print('você jogou {} e o bot {} logo'.format(jkp[jogada], jkp[bot]))
if jogada == 0:
    if bot == 0:
        print('A partida empatou')
    elif bot == 1:
        print('O bot ganhou a partida')
    elif bot == 2:
        print('você venceu!')
    else:
        print('você inseriu um valor invalido, o bot venceu!')
if jogada == 1:
    if bot == 0:
        print('você venceu!')
    elif bot == 1:
        print('A partida empatou')
    elif bot == 2:
        print('O bot ganhou a partida')
    else:
        print('você inseriu um valor invalido, o bot venceu!')
if jogada == 2:
    if bot == 0:
        print('o bot ganhou a partida')
    elif bot == 1:
        print('você venceu')
    elif bot == 2:
        print('A partida empatou')
    else:
        print('você inseriu um valor invalido, o bot venceu!')