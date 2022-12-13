cont = ('Zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um número entre 0 e 20:'))
    if n >= 0 and n <= 20:
        break
print(cont[n])