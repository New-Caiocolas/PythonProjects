times = ('Água Santa','Botafogo','Corinthians','Ferroviária','Grêmio','Novorizontino','Guarani','Inter','Limeira','Ituano')

print('-=' * 15)
print(times)
print('-=' * 15)
print(times[0:5])
print('-=' * 15)
print(times[-4:])
print('-=' * 15)
print(sorted(times))
print('-=' * 15)
print('O guarani esta em {} posição.'.format(times.index('Guarani') + 1))