def metade(n = 0):
    num = n/2
    return num

def dobro(n = 0):
    num = n*2
    return num

def aumentar(n = 0):
    a = (n/100 * 10) + n
    return a

def moeda(n = 0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')