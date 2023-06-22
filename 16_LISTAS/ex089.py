lista = []
pessoas = []
while True:
    lista.append(str(input('Digite um nome:')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    pessoas.append(lista[:])
    lista.clear()
    con = str(input('Quer continuar [S/N]:'))
    if con in 'Nn':
        break
for p in range(len(pessoas)):    
    media = (pessoas[p][1] + pessoas[p][2]) / 2
    print(p, end=' ')
    print(pessoas[p][0], end=' ')
    print(media)
while True:    
    notas = int(input('Mostrar notas de qual aluno [999 para finalizar]:'))
    if notas == '999':
        break
    print(f'As notas de {pessoas[notas][0]} foram essas {pessoas[notas][1], pessoas[notas][2]}')
    