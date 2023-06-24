pessoa = {}
pessoa['nome'] = str(input('Digite um nome:'))
pessoa['media'] = float(input('Digite a media:'))
print('-'*30)
print(f'- O nome da pessoa é {pessoa["nome"]}')
print(f'- A media de {pessoa["nome"]} é {pessoa["media"]}')
if pessoa['media'] >= 7:
    pessoa['situação'] = 'APROVADO'
elif pessoa['media'] < 5:
    pessoa['situação'] = 'REPROVADO'
else:
    pessoa['situação'] = 'RECUPERAÇÃO'
print(f'A situação do aluno é {pessoa["situação"]}')
