from random import randint
lista = []
jogos = []
tot = 1
jogo = int(input('Quantos jogos voce quer gerar:'))
while tot <= jogo:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(jogos)