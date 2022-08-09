dias = int(input('Quantidade de dias alugado:$'))
km = float(input('quilômetros rodados durante esses {} dias:'.format(dias)))
preço = ((dias * 60) +(km * 0.15))
print ('O preço do aluguel ao todo é {}reais'.format(preço))
