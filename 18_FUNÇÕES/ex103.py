def jogador(n="<desconhecido>",g=0):
    print(f'O nome do jogador é {n} e ele fez {g} gols:')
nome = str(input('digite o nome:'))
gols = str(input('digite os gols:'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    jogador(g=gols)
else:
    jogador(nome,gols)