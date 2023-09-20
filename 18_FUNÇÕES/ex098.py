def cont(a,b,c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    if iniciar < finalizar:
        contador = a
        while contador <= b:
            print(contador, end=' ') 
            contador += c
    else:
        contador = a
        while contador >= b:
            print(contador, end=' ')
            contador -= c


iniciar = int(input('número para iniciar a contagem:'))
finalizar = int(input('número para finalizar a contagem:'))
passos = int(input('Passos:'))

cont(iniciar, finalizar, passos)