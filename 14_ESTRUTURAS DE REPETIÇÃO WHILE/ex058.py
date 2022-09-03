from random import randint

nome = str(input('Digite seu nome:'))
sn = str(input('OLÁ {} VAMOS JOGAR UM JOGO (s/n):'.format(nome))).upper()
acertou = False
tentativas = 0
s = randint(0, 10)
if sn == 'S':
    print('VAMOS COMEÇAR:')
    print('=---=' * 20)
    print('VOU PENSAR EM UM NÚMERO DE 0 A 10.')
    print('=---=' * 20)

    while not acertou:
        n = int(input('TENTE ADIVINHAR AQUI:'))
        tentativas += 1
        if s == n:
            acertou = True
        else:
            if s > n:
                print('maior... tente novamente:')
            elif s < n:
                print('menor... tente novamente:')
    print('você precisou de {} tentativas para acertar.'.format(tentativas))        
else:
    print('Ok deixa para próxima!')

