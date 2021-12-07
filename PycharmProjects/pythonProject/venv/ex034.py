sal = float(input('Digite seu salário:'))
aumento10 = (sal/100 * 10) + sal
aumento15 = (sal/100 * 15) + sal
if sal > 1250.00:
    print('Você vai ter um aumento de 10% e seu salário vai passar a ser R${}'.format(aumento10))
if sal <= 1250.00:
    print('Você vai ter um aumento de 15% e seu salário vai passar a ser R${}'.format(aumento15))

