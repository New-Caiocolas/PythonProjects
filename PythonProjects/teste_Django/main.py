import requests 

link = ("https://servicodados.ibge.gov.br/api/v1/localidades/regioes/1|2|3|4|5")

requisicao = requests.get(link)
info = requisicao.json()

print(info)