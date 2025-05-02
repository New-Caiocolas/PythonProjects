import uteis

valor = float(input('Digite um valor R$:'))
print(f'O metade de {uteis.moeda(valor)} é R${uteis.moeda(uteis.metade(valor))}')
print(f'O dobro de {uteis.moeda(valor)} é R${uteis.moeda(uteis.dobro(valor))}')
print(f'O valor de {uteis.moeda(valor)} acrescentado 10% é R${uteis.moeda(uteis.aumentar(valor))}')