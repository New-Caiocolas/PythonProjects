from datetime import date

pessoas = {}
pessoas['nome'] = str(input('Digite o seu nome:'))
pessoas['ano'] = int(input('Digite seu ano de nascimento:'))
pessoas['carteira'] = int(input('Digite sua carteira de trabalho (0 NÃO TEM):'))
if pessoas['carteira'] != 0:
    pessoas['contratação'] = int(input('Digite o seu ano de contratação:'))
    pessoas['salario'] = int(input('Salário: R$'))
print('=-' * 30)
print(f'- Seu nome é: {pessoas["nome"]}')
pessoas['idade'] = date.today().year - pessoas["ano"]
print(f'- Sua idade é: {pessoas["idade"]}')
print(f'- ctps tem valor: {pessoas["carteira"]}')
if pessoas['carteira'] != 0:
    print(f'- Contratação foi em: {pessoas["contratação"]}')
    print(f'- O salário é : {pessoas["salario"]}')
    print(f'- A sua aposentadoria é com {pessoas["idade"] + (pessoas["contratação"] + 35) - date.today().year} anos')
