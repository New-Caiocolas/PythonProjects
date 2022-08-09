d = int(input('QUAL É A DISTANCIA DA SUA VIAGEM EM KM/H:'))
if d <= 200:
    print('Sua viagem vai custar R$0,50 por KM ,no total de R${} reais'.format(d*0.50))
else:
    print('Sua viagem vai custar R$0,45 por KM ,no total de R${} reais'.format(d*0.45))
