ex = str(input('Digite uma expressão: '))
lista = []
for simb in ex:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão é invalida')