from datetime import date
nas = int(input('DATA DE NASCIMENTO:'))
atual = date.today().year
idade = (2021 - nas)
alist = (18 - idade)
qnd = (2021 + alist)
alist2 = (idade - 18)
qnd2 = (2021 - alist2)
if idade < 18:
    print('você tem {} anos em {}, faltam {} anos para o seu alistamento, ele será no ano de {} '.format(idade,atual,alist,qnd))
elif idade > 18:
    print('você tem {} anos em {}, já era pra você ter se alistado a {} anos, ele seria no ano de {}'.format(idade,atual,alist2,qnd2))
else:
    print('você tem {} anos em {}, vá se alistar IMEDIATAMENTE.'.format(idade,atual))
    

