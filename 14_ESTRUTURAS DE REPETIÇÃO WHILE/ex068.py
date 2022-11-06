import random

cont = 0
while True:
    print('-='*16)
    print('Vamos jogar PAR ou IMPAR')
    print('-='*16)
    print('TOTAL DE {} VITORIAS'.format(cont))
    n = int(input('Digite um número:'))
    jogada = str(input('Deseja jogar PAR ou IMPAR[P/I]: ')).strip().upper()
    computador = random.randint(1,10)
    resultado = (n + computador) % 2
    soma = n + computador
    print(soma)
    if resultado == 1 and jogada == 'I':
        print('VOCÊ VENCEU!. O computador jogou {} e vc {} a soma entre eles é {} que é IMPAR.'.format(computador,n,soma))
    elif resultado == 0 and jogada == 'P':
        print('VOCÊ VENCEU!. O computador jogou {} e vc {} a soma entre eles é {} que é PAR.'.format(computador,n,soma))
    else:  
        break 
    cont += 1
print('você perdeu depois de {} jogos vencidos '.format(cont))