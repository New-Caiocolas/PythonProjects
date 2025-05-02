def leiaDinheiro(valor):
    valido = False
    while not valido:
        entrada = str(input(valor)).strip().replace(',','.')
        if entrada.isalpha() or not entrada:
            print(f'"{entrada}" ENTRADA INVÁLIDA!')
        else:
            valido = True
    return float(entrada)