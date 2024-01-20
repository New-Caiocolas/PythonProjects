from time import sleep

t = int(input('Quantos segundos deseja:'))

while t != 0:
    min, seg = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(min,seg)
    print(timer, end='\r')
    t -= 1
    sleep(1)

     