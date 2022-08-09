v = int(input('Digite a velocidade do seu carro em KM/h:'))
a = v - 80
if v > 80:
    print('MULTADO! ,o senhor estava a {}km/h acima do limite'.format(a))
    print('Sua multa custará R${} reais'.format(a*7))
    print('TENHA UM BOM DIA DIRIJA COM SEGURANÇA!')
else:
    print('Parabéns você estava dentro do limite de 80km/h')
