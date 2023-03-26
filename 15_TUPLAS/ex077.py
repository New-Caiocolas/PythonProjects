palavras = ('APRENDER', 'PYTHON', 'PROGAMAR', 'LINGUAGEM', 'CURSO')
for p in palavras:
    print('\nNa palavra {} temos:'.format(p), end=' ')
    for v in p:
        if v.lower() in 'aeiou':
            print(v,end='')