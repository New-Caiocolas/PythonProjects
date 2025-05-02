def metade(n = 0, formato=False):
    num = n/2
    return num if formato is False else moeda(num)

def dobro(n = 0, formato=False):
    num = n*2
    return num if formato is False else moeda(num)

def aumentar(n = 0,  formato=False):
    a = (n/100 * 10) + n
    return a if formato is False else moeda(a)

def moeda(n = 0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')