print('=-'*20)
print('LOJA SUPER BARATÃO')
print('=-'*20)
total = 0
produtocaro = 0
cont = 0
barato = 0
nomep = ''
while True:
    produto = str(input('Qual é o nome do produto:'))
    valor = int(input('Qual é o valor:'))
    c = str(input('Deseja continuar:[S/N]')).upper().strip()
    total += valor
    cont += 1
    if cont == 1:
        barato = valor
        nomep = produto
    else:
        if barato > valor:
            barato = valor
            nomep = produto
    if valor > 1000:
        produtocaro += 1
    if c == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('O total da compra foi R${:.2f}.'.format(total))
print('Temos {} produtos que custam mais de R$1000'.format(produtocaro))
print('O produto mais barato foi {} que custa R${}'.format(nomep,barato))