def leiaInt(msg):
    while True:
        try:
            n  = int(input(msg))
            return n
        except (ValueError,TypeError):
            print("\033[31mERRO! Digite um valor INTEIRO válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mERRO! O usúario preferiu nao digitar\033[m")
            continue

def div():
    print('-'*40)

def cabecalho(nome):
    div()
    print(nome.center(40))
    div()

def opcao(op):
    div()
    print(f'OPÇÃO {op}'.center(40))
    div()

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[93m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    div()
    op = leiaInt('OPERAÇÃO:')
    return op

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO AO CRIAR ARQUIVO')
    else:
        print(f'ARQUIVO {nome} criado com sucesso!!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def escreverArquivo(nomearq,nome='desconhecido',idade=0):
    try:
        a = open(nomearq, 'at')
    except:
        print('ERRO ao escrever arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('HOUVE UM ERRO ao escrever os dados!')
        else:
            print(f'NOVO REGISTRO DE {nome} ADICIONADO!')
            a.close()