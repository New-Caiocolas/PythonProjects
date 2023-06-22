matriz = [[0 ,0 ,0],[0 ,0 ,0],[0 ,0 ,0]]
spar = scol = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um número para posição [{l},{c}]:'))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*30)
for l in range(0,3):
    scol += matriz[l][2]
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(spar)
print(scol)
print(maior)