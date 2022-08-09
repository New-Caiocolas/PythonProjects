n = int(input('DIGITE UM NÚMERO:'))
r = n % 2
if r == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))