'''def leiaInt(msg):
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
print(f'Você digitou {n}!')'''

def leiaInt(msg):
    while True:
        try:
            n  = int(input(msg))
            return print(f'O valor digitado foi {n}')
        except (ValueError,TypeError):
            print("\033[31mERRO! Digite um valor INTEIRO válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mERRO! O usúario preferiu nao digitar\033[m")
            continue

def leiaFloat(msg):
    while True:
        try:
            n  = float(input(msg))
            return print(f'O valor digitado foi {n}')
        except (ValueError,TypeError):
            print("\033[31mERRO! Digite um valor real válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mERRO! O usúario preferiu nao digitar\033[m")
            continue

num = leiaFloat("digite um valor:")