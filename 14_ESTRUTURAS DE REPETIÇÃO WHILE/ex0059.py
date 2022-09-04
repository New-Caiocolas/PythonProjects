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
        print('a soma entre {} e {} e igual a {}'.format(n1,n2,soma))
    if op == 2:
        mult = n1 * n2
        print('a multiplicacao entre {} e {} e igual a {}'.format(n1,n2,mult))
    if op == 3:
        if n1 > n2:
            print('o numero {} e maior que {}'.format(n1,n2))
        elif n1 < n2:
            print('o numero {} e maior que {}'.format(n2,n1))
        else:
            print('os numeros sao iguais ou seja o maior e ele mesmo {}'.format(n1))
    if op == 4:
        n1 = int(input('digite um número:'))
        n2 = int(input('digite outro número:'))
    if op == 5:
        ver = True
    if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('dados invalidos... tente novamente.')
print('programa finalizado com sucesso')