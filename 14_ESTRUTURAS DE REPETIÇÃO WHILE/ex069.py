de_maior = 0
masc = 0
mulheridade = 0
while True:
    idade = int(input('Digite a idade da pessoa:'))
    sexo = str(input('digite o sexo da pessoa [M/F]:')).strip().upper()
    c = str(input('Deseja continuar [S/N]:')).strip().upper()
    if idade > 18:
        de_maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        mulheridade += 1
    if c == 'N':
        break
print('{} pessoas tem mais de 18 anos, {} homens foram cadastrados e {} mulheres tem menos de 20 anos'.format(de_maior, masc, mulheridade))