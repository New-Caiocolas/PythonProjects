import random

print('password generator')
chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,+=1234567890')
quantity = int(input('quantas senhas você deseja:'))
character = int(input('quantos caracteres você deseja:'))
print('suas senhas:')
for pwd in range (quantity):
    passwords = ''
    for c in range(character):
        passwords += random.choice(chars)
    print(passwords)
