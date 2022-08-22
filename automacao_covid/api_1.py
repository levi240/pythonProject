import json,csv
import urllib.request

#def localizaDados(jogo,)

try:
    html = urllib.request.urlopen('https://servicebus2.caixa.gov.br/portaldeloterias/api/quina/5895')
    texto=html.read().decode("utf-8")
    dicionario={texto}
    arquivo = open("megasena.json","w")
    if arquivo:
        print("arquivo salvo com sucesso")
        arquivo.write(texto)
        arquivo.close()
    else:
        "Falha ao salvar arquivo"
except("falha"):
    print("erro")
finally:
    print("ok")


invalido=[]
valido=[]
with open("megasena.json","r+") as json:
    for i in json:
       # print(i.strip("\n\n"))
        invalido.append(i.strip("\n\n").split(','))
for x in invalido:
    for y in x:
        #print(y.strip("\n"))
        valido.append(y.strip("\n"))
teste=[]
for t in valido:
    if t!='':
        teste.append(t)
print(teste)