from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1 , 7 + 1):
    ano = int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    idade = (atual - ano)
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Das 7 pessoas {} são de maiores de idade e {} são menores de idade'.format(totmaior, totmenor))
