while True:
    n = int(input('Quer ver a tabuada de qual número:'))
    if n <= 0:
        break
    else:
        for c in range(1,11):
            print('{} x {} = {}'.format(n,c,(n*c)))
print('Programa tabuada encerrado.')