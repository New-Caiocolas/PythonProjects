sexo = str(input('digite o seu sexo:')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos,qual é o seu sexo: [M/F]')).upper().strip()[0]
if sexo == 'M':
    print('sexo masculino registrado com sucesso')
elif sexo == 'F':
    print('sexo feminino registrado com sucesso')