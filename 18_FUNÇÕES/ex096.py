def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é {area}m2')


l = float(input('Digite a largura:'))
c = float(input('Digite o comprimento:'))
area(l, c)