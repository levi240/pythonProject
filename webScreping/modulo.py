from bs4 import BeautifulSoup
import requests,time,os

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

clear()

def tempo(valor):
    while True:
        print('1 - Previsão para agora')
        print('2 - Previsão para hoje')
        print('3 - Previsão para amanhã')
        print('4 - Previsão para fim de semana')
        menu = int(input('\nSelecione a opção desejada : '))
        #menu = valor
        if menu == 1:
            time.sleep(valor)
            html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/442/ferrazdevasconcelos-sp').content
            soup = BeautifulSoup(html, 'html.parser')
            regiao = soup.find(class_="-bold -font-18 -dark-blue")
            maxTemp = soup.find(class_="-bold -gray-dark-2 -font-55 _margin-l-20 _center")
            minTemp = soup.find("span", id="min-temp-1")
            clear()
            print(f"\n\n{regiao.text.strip()} {maxTemp.string.strip()} Graus.\n\n")
        elif menu==2:
            time.sleep(valor)
            html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/442/ferrazdevasconcelos-sp').content
            soup = BeautifulSoup(html, 'html.parser')
            regiao = soup.find(class_="-bold -font-18 -dark-blue _margin-r-10 _margin-b-sm-5").text
            titulo = regiao.strip().split()
            tx=''
            maxTemp = soup.find("span", id="max-temp-1")
            minTemp = soup.find("span", id="min-temp-1")
            for texto in (titulo):
                tx+=(texto)+' '
            clear()
            print(f'\n\n{tx} Máxima {maxTemp.string.strip()} e Minima de {minTemp.string.strip()} Graus \n\n')
        elif menu==3:
            time.sleep(valor)
            html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/amanha/cidade/442/ferrazdevasconcelos-sp').content
            soup = BeautifulSoup(html, 'html.parser')
            regiao = soup.find(class_="-bold -font-18 -dark-blue _margin-r-10 _margin-b-sm-5").text
            titulo = regiao.strip().split()
            tx = ''
            maxTemp = soup.find("span", id="max-temp-1")
            minTemp = soup.find("span", id="min-temp-1")
            for texto in (titulo):
                tx += (texto) + ' '
            clear()
            print(f'\n\n{tx} Máxima {maxTemp.string.strip()} e Minima de {minTemp.string.strip()} Graus \n\n')
        elif menu==4:
            time.sleep(valor)
            cidade=[]
            tempMax=[]
            tempMin=[]
            html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/fim-de-semana/cidade/442/ferrazdevasconcelos-sp').content
            soup = BeautifulSoup(html, 'html.parser')
            for text in soup.findAll(class_="-bold -font-18 -dark-blue"):
                cidade.append(text.text)
            for max in soup.findAll(class_="max-temp"):
                tempMax.append(max.text)
            for min in soup.findAll(class_="min-temp"):
                tempMin.append(min.text)
            maxTemp = [tempMax[0], tempMax[2]]
            minTemp = [tempMin[0], tempMin[2]]
            clear()
            for result in range(len(cidade)):
                print(f'{cidade[result]} Máxima {maxTemp[result]} Mínima {minTemp[result]} Graus')
            #print(f'{cidade[0],tempMax[0],tempMin[0]}')
        else:
            print("Saindo do sistema")
            break
while True:
    tempo(1)

