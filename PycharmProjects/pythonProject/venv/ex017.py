from math import hypot
a = float(input('Cateto oposto:'))
b = float(input('Cateto adjascente:'))
hi = hypot(a,b)
print('A hipotenusa vai medir {:.2f}'.format(hi))