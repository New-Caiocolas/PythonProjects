import __init__ as init
from time import sleep

arquivo = "pessoas.txt" ## txt file name

# checks if the file does not exist and creates the file
if not init.arquivoExiste(arquivo):
    init.criarArquivo(arquivo)
    
while True:
    ## menu configuration
    op = init.menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema']) 
    if op == 1:
        init.cabecalho('LISTA DE RESGISTROS') ## write the header
        init.lerArquivo(arquivo) ## list registered people
    elif op == 2:
        init.cabecalho('NOVO RESGISTRO') ## write the header
        nome = str(input('Digite o nome: '))
        idade = init.leiaInt('Digite a idade: ')
        init.escreverArquivo(arquivo,nome,idade)
    elif op == 3:
        print('SAINDO DO SISTEMA!')
        break
    else:
        print('\033[31mDigite uma opção válida\033[m')
    sleep(1)
    