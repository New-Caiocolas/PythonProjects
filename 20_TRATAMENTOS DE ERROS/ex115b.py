import __init__ as init
from pathlib import Path
from time import sleep


while True:
    sleep(1)
    op = init.menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    arquivo = Path("pessoas.txt")
    if op == 1:
        init.opcao(1)
        print(arquivo.read_text())
    elif op == 2:
        init.opcao(2)
        nome = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))
        with arquivo.open(mode="a", encoding="utf-8") as arquivo:
            arquivo.write(f'{nome};{idade}\n')
    elif op == 3:
        print('op 3')
        break
    else:
        print('\033[31mDigite uma opção válida\033[m')
    
