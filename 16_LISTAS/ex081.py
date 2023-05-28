list = []
while True:
    n = int(input('digite um número:'))
    list.append(n)
    con = str(input('Quer continuar S/N:'))
    if con in "Nn":
        break

print(f'Você digitou {len(list)} elementos')
list.sort(reverse = True)
print(list)
if 5 in list:
    print('O valor 5 esta na lista')
else:
    print('Não existe nenhum valor 5 na lista')
