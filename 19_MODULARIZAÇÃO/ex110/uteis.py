def metade(n = 0, formato=False):
    num = n/2
    return num if formato is False else moeda(num)

def dobro(n = 0, formato=False):
    num = n*2
    return num if formato is False else moeda(num)

def aumentar(n = 0, percent=0,  formato=False):
    a = (n/100 * percent) + n
    return a if formato is False else moeda(a)

def moeda(n = 0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

def resumo(n,int):
    return print(f' Preço analizado: {n} \n Metade do preço: {metade(n)} \n Dobro do preço: {dobro(n)} \n Aumentar {int}%: {aumentar(n,int)}')