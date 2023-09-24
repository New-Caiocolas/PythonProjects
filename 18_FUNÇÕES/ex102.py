def fatorial(a, show=False):
    '''
    -> Calculam o Fatorial
    Para n: Número a ser calculado.
    Para show: Se for True informa o calculo do fatorial e False não.
    Return F: Retorna o valor do fatorial.
    '''
    f = 1
    for c in range(a, 0, -1):
        f *= c
        if show:
            if c >= 1:
                print(f'{c}', end='')
                print(' x ', end='')
            else:
                print('= ', end='')
    return f    


print(fatorial(5,True))