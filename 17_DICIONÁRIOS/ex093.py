jogador = {}
lista = []
total = 0
jogador['nome'] = str(input('Digite seu nome: '))
partidas = int(input('Digite a quantidade de partidas: '))
for p in range(partidas):
    gols = int(input(f'Quantos gols na partida {p+1}: '))
    lista.append(gols)
    total += gols
jogador['gols'] = lista
jogador['total'] = total
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'   ==> Na partida {k} fez {v} gols')
print(f'Foi um total de {total} gols')