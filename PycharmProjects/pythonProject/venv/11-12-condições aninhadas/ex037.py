num = int(input('digite um numero inteiro: '))
print('''escolha uma das base de conversão
[1] converter pra binário
[2] converter pra octal
[3] converter pra hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para binário {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para octal {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para hexadecimal {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida, tente novamente. ')