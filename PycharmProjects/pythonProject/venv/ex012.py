preço = float(input('digite o preço de um produto R$'))
a = (preço * 5 / 100)
novo = (preço - a)
print('{} reais com 5% de desconto é {} reais'.format(preço,novo))