import math
an = float(input('Digite seu ângulo:'))
seno = math.sin(math.radians(an))
coss = math.cos(math.radians(an))
tann = math.tan(math.radians(an))
print('O angulo {} tem o SENO {:.2f}'.format(an,seno))
print('O angulo {} tem o COSSENO {:.2f}'.format(an,coss))
print("O angulo {} tem a TANGENTE {:.2f}".format(an,tann))