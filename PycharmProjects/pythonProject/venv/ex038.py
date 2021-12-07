num1 = int(input('digite o primeiro número:'))
num2 = int(input('digite o segundo número:'))
if num1 > num2:
     print('{} é maior do que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior do que {}'.format(num2, num1))
else:
    print('{} é igual a {}'.format(num1, num2))