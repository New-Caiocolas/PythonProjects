v = float(input("QUAL É O VALOR DA CASA:"))
s = float(input("QUAL É O SEU SÁLARIO:"))
a = int(input("EM QUANTOS ANOS VOCÊ PRETENDE PAGAR:"))
mes = v / (a * 12)
sa = (s / 100)*30
if sa <= v:
    print("O emprestimo pode ser CONCEDIDO e você pagará {:.2f} por mês durante um período de {} anos.".format(mes,a))
else:
    print("O emprestimo não pode ser concedido.")
