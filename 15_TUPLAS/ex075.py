num = (int(input('Digite um número:')),
int(input('Digite outro número:')),
int(input('Digite mais um número:')),
int(input('Digite o ultimo número:')))
print('Você digitou os números {}'.format(num))
print('O valor 9 apareceu {}x'.format(num.count(9)))
if 3 in num:
    print('O valor 3 foi encontrado na posição {}'.format(num.index(3)+1))
else:
    print('O valor 3 não foi encontrado')
print('O valores pares são:',end='')
for n in num:
    if n % 2 == 0:
        print('{} '.format(n), end='')