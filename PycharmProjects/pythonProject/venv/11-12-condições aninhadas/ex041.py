from datetime import date
ano = int(input('ANO DE NASCIMENTO: '))
atual = date.today().year
idade = (atual - ano)

print('O atleta com {} anos,vai competir na categoria:'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade <= 14 and idade > 9:
    print('INFANTIL')
elif idade <= 19 and idade > 14:
    print('JÚNIOR')
elif idade <= 25 and idade > 19:
    print('SÊNIOR')
else:
    print('MASTER')
