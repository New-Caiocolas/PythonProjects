val = []
maior = 0
menor = 0
for v in range(0,5):
    val.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = val[v]
    else:
        if val[v] > maior:
            maior = val[v]
        if val[v] < menor:
            menor = val[v]
print(f'o maior valor é {maior} nas posições: ', end='')
for i, c in enumerate(val):
    if c == maior:
        print(f'{maior}', end='...')
print()
print(f'o menor valor é {menor} nas posições')

