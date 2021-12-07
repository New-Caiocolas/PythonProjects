n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
print('Tirando {} e {} , a media será {:.1f}'.format(n1,n2,media))
if media > 7.0:
    print('VOCÊ ESTÁ APROVADO')
elif media > 5.0 and media <= 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO')
else:
    print('REPROVADO') 

