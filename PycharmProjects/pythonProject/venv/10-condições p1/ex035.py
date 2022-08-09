print('=--=' * 20)
print('ANALIZADOR DE TRIÂNGULOS')
print('=--=' * 20)

reta1 = int(input('Digite a primeira reta:'))
reta2 = int(input('Digite a segunda reta:'))
reta3 = int(input('Digite a terceira reta:'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar triângulo.')
else:
    print('Os segmentos acima não podem formar triângulo.')
