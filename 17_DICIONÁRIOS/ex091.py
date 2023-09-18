from random import randint
from time import sleep

c = 1
dados = {
    'pessoa1': randint(1,6),
    'pessoa2': randint(1,6),
    'pessoa3': randint(1,6),
    'pessoa4': randint(1,6)
}
rank = {}

for k,v in dados.items():
    print(f'A {k} jogou o dado e caiu {v}')
    sleep(1)
print('-'*30)

rank = dict(sorted(dados.items(), key=lambda item: item[1], reverse=True))

for k,v in rank.items():
    print(f'{c}o lugar foi a {k} com {v}')
    c += 1
    sleep(1)