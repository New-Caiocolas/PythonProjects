def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a
    if idade < 16:
        return f'COM {idade} ANOS: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'COM {idade} ANOS: VOTO OPCIONAL'
    else:
        return f'COM {idade} ANOS: VOTO OBRIGATÓRIO'


ano = int(input('Digite o ano que vc nasceu:'))
print(voto(ano))