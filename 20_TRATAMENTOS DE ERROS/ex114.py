import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except (urllib.error.URLError):
    print('ERRO! o site não está acessível no momento')
else:
    print('TUDO ÓTIMO, o site está acessivel')