from utilidadesCeV import moeda
from utilidadesCeV import dado

valor = dado.leiaDinheiro('Digite um preço:R$')
moeda.resumo(valor,20,True)