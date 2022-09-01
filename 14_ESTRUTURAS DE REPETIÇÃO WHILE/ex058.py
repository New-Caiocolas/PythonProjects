import random

nome = str(input('Digite seu nome:'))
sn = str(input('OLÁ {} VAMOS JOGAR UM JOGO (s/n):'.format(nome))).upper()
n = -1
tentativas = 0
if sn == 'S':
    print('VAMOS COMEÇAR:')
    print('=---=' * 20)
    print('VOU PENSAR EM UM NÚMERO DE 0 A 10.')
    print('=---=' * 20)
    s = random.randint(0, 10)

    while n != s:
        n = int(input('TENTE ADIVINHAR AQUI:'))
        tentativas += 1
        if s == n:
            print('PARABÉNS MERO MORTAL VC ME DERROTOU!')
        else:
            print('ERROU, TENTE NOVAMENTE!')
    print('você precisou de {} tentativas para acertar.'.format(tentativas))        
else:
    print('Ok deixa para próxima!')

