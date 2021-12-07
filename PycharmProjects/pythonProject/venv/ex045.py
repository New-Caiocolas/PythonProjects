from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
SUAS OPÇÕES:
-=-=-=-=-=-=-=-=-=-=-=-=-=-
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
jogador = int(input('Qual é a sua jogada:'))
print('JO!')
sleep(1)
print('KEN!!')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('COMPUTADOR JOGOU  {}'.format(itens[computador]))
print('JOGADOR JOGOU  {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('A PARTIDA EMPATOU!')
    elif jogador == 1:
        print('O JOGADOR GANHOU!')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU!')
    else:
        print('VOCÊ DIGITOU UM VALOR INVALIDO LOGO O COMPUTADOR VENCEU!')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('A PARTIDA EMPATOU!')
    elif jogador == 2:
        print('O JOGADOR GANHOU!')  
    else:
        print('VOCÊ DIGITOU UM VALOR INVALIDO LOGO O COMPUTADOR VENCEU!')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR GANHOU!')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('A PARTIDA EMPATOU!')
    else:
        print('VOCÊ DIGITOU UM VALOR INVALIDO LOGO O COMPUTADOR VENCEU!')
