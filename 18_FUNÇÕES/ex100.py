from random import randint


def sortear():
    while len(lista) < 5:
        lista.append(randint(1,10))
    print(lista)


def somapar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)
 
lista = []
sortear()
somapar()