def leiaDinheiro(valor):
    valido = False
    while not valido:
        entrada = str(input('Digite um valor: R$')).strip()
        if entrada.isalpha() or not entrada:
            print(f'"{entrada}" ENTRADA INVÁLIDA!')
    