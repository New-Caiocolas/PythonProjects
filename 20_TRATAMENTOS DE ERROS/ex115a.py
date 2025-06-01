import __init__ as init


while True:
    op = init.menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if op == 1:
        print('op 1')
    elif op == 2:
        print('op 2')
    elif op == 3:
        print('op 3')
        break
    else:
        print('\033[31mDigite uma opção válida\033[m')
