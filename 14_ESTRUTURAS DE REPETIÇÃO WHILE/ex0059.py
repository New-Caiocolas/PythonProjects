from time import sleep

n1 = int(input('digite um número:'))
n2 = int(input('digite outro número:'))
ver = False
while not ver:
    sleep(0.5)
    print('=---=' * 20)
    print('''
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
''')
    op = int(input('oque você deseja:'))
    if op == 1:
        soma = n1 + n2 
        print('a soma entre {} + {} e igual a {}'.format(n1,n2,soma))
    elif op == 2:
        mult = n1 * n2
        print('a multiplicacao entre {} x {} e igual a {}'.format(n1,n2,mult))
    elif op == 3:
        if n1 > n2:
            print('o numero {} e maior que {}'.format(n1,n2))
        elif n1 < n2:
            print('o numero {} e maior que {}'.format(n2,n1))
        else:
            print('os numeros sao iguais ou seja o maior e ele mesmo {}'.format(n1))
    elif op == 4:
        n1 = int(input('digite um número:'))
        n2 = int(input('digite outro número:'))
    elif op == 5:
        ver = True
    else:
        print('dados inválidos... tente novamente.')
print('programa finalizado com sucesso')