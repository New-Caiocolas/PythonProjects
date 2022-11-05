s = cont = 0
while True:
    n = int(input('digite um número [999 para parar] '))
    if n == 999:
        break
    s += n
    cont += 1
print('vc digitou {} números e a soma entre eles é {} '.format(cont, s))