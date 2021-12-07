frase = str(input('Digite uma frase:')).upper().strip()

print('A letra a A na sua frase se repete {} vezes '.format(frase.count('A')))
print ('A primeira vez que a letra A aparece na frase foi  na posição {}'.format(frase.find('A')+1))
print ('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))
