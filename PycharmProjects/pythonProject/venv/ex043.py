peso = int(input('Digite seu peso (Kg)'))
alt = float(input('Digite sua altura (M)'))
imc = peso / (alt ** 2)
print('DE ACORDO COM SUA ALTURA QUE É {} E SEU PESO {}'.format(alt,peso))
print('SEU IMC É {:.1f}'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO')
elif imc < 25:
    print('VOCÊ ESTÁ COM O PESO IDEAL')
elif imc < 30:
    print('VOCÊ ESTÁ COM SOBREPESO')
elif imc < 40:
    print('VOCÊ ESTÁ COM OBESIDADE')
else:
    print('VOCÊ ESTÁ COM OBESIDADE MÓRBIDA! CUIDADO!')        


