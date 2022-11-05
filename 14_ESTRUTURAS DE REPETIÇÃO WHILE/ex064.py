n = 0
cont = -1
soma = -999
while n != 999:
    n = int(input('digite um número [999 para parar]:'))
    soma += n
    cont += 1
if cont <= 0:
    print('vc nao digitou valor nenhum.')
else:
    print('vc digitou {} números e a soma entre eles é {}'.format(cont, soma))