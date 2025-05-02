import uteis

formato = False
valor = float(input('Digite um valor R$:'))
formatar = str(input('Deseja formatar (S/N):'))
if formatar in 'Ss':
    formato = True
print(f'O metade de {uteis.moeda(valor)} é R${uteis.metade(valor,formato)}')
print(f'O dobro de {uteis.moeda(valor)} é R${uteis.dobro(valor,formato)}')
print(f'O valor de {uteis.moeda(valor)} acrescentado 10% é R${uteis.aumentar(valor,formato)}')24