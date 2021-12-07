import random

nome = str(input('Digite seu nome:'))
sn = str(input('OLÁ {} VAMOS JOGAR UM JOGO (s/n):'.format(nome))).upper()

if sn == 'S':
    print('VAMOS COMEÇAR:')
    print('=---=' * 20)
    print('VOU PENSAR EM UM NÚMERO DE 0 A 5.')
    print('=---=' * 20)

    n = int(input('TENTE ADIVINHAR AQUI:'))
    s = random.randint(0, 5)

    if s == n:
        print('PARABÉNS MERO MORTAL VC ME DERROTOU!')
    else:
        print('ERROU A RESPOSTA ERA {}, TENTE NOVAMENTE!'.format(s))
            
else:
    print('Ok deixa para próxima!')




