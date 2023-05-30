pessoas = []
info = []
mai = men = 0
while True:
    info.append(str(input('Digite seu nome:')))
    info.append(float(input('Digite seu peso:')))
    if len(pessoas) == 0:
        mai = men = info[1]
    else:
        if info[1] > mai:
            mai = info[1]
        if info[1] < men:
            men = info[1]
    con = str(input('Quer continuar S/N:'))
    pessoas.append(info[:])
    info.clear()
    if con in 'Nn':
        break
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {mai}kg e dessas pessoas:', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{ p[0] }', end='')
print()
print(f'O menor peso foi {men}kg e dessas pessoas',end='')
for p in pessoas:        
    if p[1] == men:
        print(f'{ p[0] }', end='')	
