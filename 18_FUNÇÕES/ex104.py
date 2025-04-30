def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um número válido!')
        if ok:
            break
    return valor
n = leiaInt('Digite umm valor:')
print(f'Você digitou {n}!')
