nome = str(input('Digite seu nome completo')).strip()
print ('Seu nome em letras MAIUSCULAS é {}'.format(nome.upper()))
print ('Seu nome em letras MINUSCULAS é {}'.format(nome.lower()))
print ('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras '.format(nome.find(' ')))