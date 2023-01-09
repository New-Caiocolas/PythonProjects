from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram:', end='')
for c in n:
    print(c , end=' ')
print('\nO maior valor é:{}'.format(max(n)))
print('O menor valor é:{}'.format(min(n)))