print('-'*35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-'*35)
lista = ('lápis', 1.75,'borracha', 2,'caderno', 15.90,'caneta', 1.75)
for item in range(0,len(lista)):
    if item % 2 == 0:
        print('{:.<28}'.format(lista[item]), end='')
    else:
        print('{:.>5.2f}'.format(lista[item]))
print('-'*35)